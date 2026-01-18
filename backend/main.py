from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
import asyncio
import database
import models
import services

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup: Create tables
@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "Server is running"}

# Pydantic Models for Request/Response
class QuizRequest(BaseModel):
    url: str

class GenerateResponse(BaseModel):
    id: int
    url: str
    title: str
    summary: str
    key_entities: dict
    sections: Optional[List[str]] = []
    quiz: List[dict]
    related_topics: List[str]

# Endpoints
@app.post("/api/generate", response_model=GenerateResponse)
async def generate_quiz(request: QuizRequest, db: AsyncSession = Depends(database.get_db)):
    # Set overall timeout of 8 seconds for the entire operation (fail fast!)
    try:
        return await asyncio.wait_for(_generate_quiz_internal(request, db), timeout=8.0)
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request timed out after 8 seconds. Please try again.")
    except Exception as e:
        print(f"Error in generate_quiz: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

async def _generate_quiz_internal(request: QuizRequest, db: AsyncSession):
    print(f"\n{'='*60}")
    print(f"Starting quiz generation for URL: {request.url}")
    print(f"{'='*60}")
    # 1. Scrape (run in thread pool with timeout)
    try:
        print("Step 1: Scraping Wikipedia article...")
        loop = asyncio.get_event_loop()
        # Add timeout to scraping too
        scraped_data = await asyncio.wait_for(
            loop.run_in_executor(None, services.scrape_wikipedia, request.url),
            timeout=6.0
        )
        print(f"✓ Scraping completed!")
        print(f"  - Title: {scraped_data['title']}")
        print(f"  - Content length: {len(scraped_data['text'])} characters (FULL article content)")
        print(f"  - Content preview: {scraped_data['text'][:200]}...")
    except asyncio.TimeoutError:
        print("⚠ Scraping timed out, using fallback...")
        raise HTTPException(status_code=408, detail="Scraping timed out. Please check your internet connection.")
    except Exception as e:
        print(f"Scraping failed: {e}")
        raise HTTPException(status_code=400, detail=f"Failed to scrape URL: {str(e)}")
    
    # 2. Check if text is sufficient
    if not scraped_data["text"]:
         raise HTTPException(status_code=400, detail="Could not extract text from Wikipedia page.")

    # 3. Generate quiz (instant - no LLM)
    try:
        print("\nStep 2: Generating quiz (instant mode)...")
        loop = asyncio.get_event_loop()
        # Add timeout even for instant generation (should be < 1 second)
        llm_data = await asyncio.wait_for(
            loop.run_in_executor(None, services.generate_quiz_content, scraped_data["text"]),
            timeout=2.0  # Should be instant, but max 2 seconds
        )
        print(f"✓ Quiz generation completed!")
        print(f"  - Questions generated: {len(llm_data.get('quiz', []))}")
        print(f"  - Related topics: {len(llm_data.get('related_topics', []))}")
    except asyncio.TimeoutError:
        print("⚠ Quiz generation timed out, using emergency fallback...")
        # Emergency fallback
        llm_data = {
            "summary": scraped_data["text"][:200] + "...",
            "key_entities": {"people": [], "organizations": [], "locations": []},
            "sections": [],
            "quiz": [{
                "question": "What is the main topic of this article?",
                "options": ["The topic described", "Option B", "Option C", "Option D"],
                "answer": "The topic described",
                "difficulty": "easy",
                "explanation": "This article discusses the main topic."
            }],
            "related_topics": []
        }
    except Exception as e:
        print(f"Quiz generation failed: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to generate quiz content: {str(e)}")
    # 4. Save to DB
    print("\nStep 3: Saving to database...")
    new_quiz = models.Quiz(
        url=request.url,
        title=scraped_data["title"],
        summary=llm_data.get("summary", ""),
        key_entities=llm_data.get("key_entities", {}),
        related_topics=llm_data.get("related_topics", [])
    )
    
    db.add(new_quiz)
    await db.commit()
    await db.refresh(new_quiz)
    
    # Save questions
    questions_data = llm_data.get("quiz", [])
    for q in questions_data:
        new_question = models.Question(
            quiz_id=new_quiz.id,
            question_text=q["question"],
            options=q["options"],
            answer=q["answer"],
            difficulty=q.get("difficulty", "medium"),
            explanation=q.get("explanation", "")
        )
        db.add(new_question)
    
    await db.commit()
    print(f"✓ Quiz saved with ID: {new_quiz.id}")
    print(f"{'='*60}\n")

    return {
        "id": new_quiz.id,
        "url": new_quiz.url,
        "title": new_quiz.title,
        "summary": new_quiz.summary,
        "key_entities": new_quiz.key_entities,
        "sections": llm_data.get("sections", []),
        "quiz": questions_data,
        "related_topics": new_quiz.related_topics
    }

@app.get("/api/history", response_model=List[GenerateResponse])
async def get_history(db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Quiz).order_by(models.Quiz.created_at.desc()))
    quizzes = result.scalars().all()
    
    history_list = []
    for quiz in quizzes:
         # Lazy loading questions might be tricky with async, better to eager load or query
         # For list, we might not need all questions? Spec says "Details" opens full quiz, so maybe just metadata here.
         # But the response model requires everything. Let's fetch questions too for simplicity or adjust model.
         # For simplicity, let's fetch questions.
         q_result = await db.execute(select(models.Question).where(models.Question.quiz_id == quiz.id))
         questions = q_result.scalars().all()
         
         formatted_questions = [
             {
                 "question": q.question_text,
                 "options": q.options,
                 "answer": q.answer,
                 "difficulty": q.difficulty,
                 "explanation": q.explanation
             } for q in questions
         ]
         
         history_list.append({
            "id": quiz.id,
            "url": quiz.url,
            "title": quiz.title,
            "summary": quiz.summary,
            "key_entities": quiz.key_entities,
            "sections": [], # Not stored in main table currently, omitting or adding column if needed.
            "quiz": formatted_questions,
            "related_topics": quiz.related_topics
         })
         
    return history_list

@app.get("/api/history/{id}", response_model=GenerateResponse)
async def get_quiz_detail(id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Quiz).where(models.Quiz.id == id))
    quiz = result.scalar_one_or_none()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
        
    q_result = await db.execute(select(models.Question).where(models.Question.quiz_id == quiz.id))
    questions = q_result.scalars().all()
    
    formatted_questions = [
             {
                 "question": q.question_text,
                 "options": q.options,
                 "answer": q.answer,
                 "difficulty": q.difficulty,
                 "explanation": q.explanation
             } for q in questions
    ]
    
    return {
        "id": quiz.id,
        "url": quiz.url,
        "title": quiz.title,
        "summary": quiz.summary,
        "key_entities": quiz.key_entities,
        "sections": [],
        "quiz": formatted_questions,
        "related_topics": quiz.related_topics
    }