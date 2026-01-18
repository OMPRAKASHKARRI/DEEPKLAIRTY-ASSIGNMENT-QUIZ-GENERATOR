import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def scrape_wikipedia(url: str):
    """
    Scrape content from a Wikipedia article URL.
    Extracts title, headings, and paragraph content.
    """
    try:
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL format. Must start with http:// or https://")
        
        if 'wikipedia.org' not in url.lower():
            print(f"Warning: URL does not appear to be a Wikipedia article: {url}")
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        print(f"Fetching URL: {url}")
        response = requests.get(url, headers=headers, timeout=5)  # 5 second timeout - fail fast!
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title_elem = soup.find('h1', {'id': 'firstHeading'})
        if not title_elem:
            raise ValueError("Could not find article title")
        title = title_elem.text.strip()
        
        # Extract content (paragraphs)
        content_div = soup.find('div', {'id': 'mw-content-text'})
        if not content_div:
            raise ValueError("Could not find article content")
        
        # Extract ALL paragraphs - get complete article content
        paragraphs = content_div.find_all('p')
        # Filter out reference sections but keep all meaningful content
        filtered_paragraphs = [
            p.text.strip() for p in paragraphs 
            if p.text.strip() and len(p.text.strip()) > 30  # Keep paragraphs with some content
            and not p.find_parent('div', class_=lambda x: x and ('reference' in x.lower() or 'navbox' in x.lower() or 'infobox' in x.lower()))
        ]
        text_content = "\n".join(filtered_paragraphs)
        
        # Also extract section headings for better context
        headings = content_div.find_all(['h2', 'h3'])
        if headings:
            heading_text = "\n".join([h.text.strip() for h in headings if h.text.strip()])
            text_content = heading_text + "\n\n" + text_content
        
        # Use FULL content - no truncation for comprehensive quiz generation
        # The smart generator can handle longer text efficiently
        print(f"  - Extracted {len(text_content)} characters of content")
        
        if not text_content:
            raise ValueError("No text content extracted from article")
        
        return {
            "title": title,
            "text": text_content
        }
    except Exception as e:
        print(f"Error scraping Wikipedia: {e}")
        raise e

def generate_quiz_content(text: str):
    """
    Generate quiz content - INSTANT MODE: Uses smart pattern-based generator.
    No LLM calls - instant response! Returns questions based on article content.
    """
    # ALWAYS use fast smart generator - it's instant and creates real questions from content!
    print("  - Using instant smart quiz generator (no API delay)...")
    return _generate_smart_quiz(text)

def _generate_smart_quiz(text: str):
    """
    INSTANT quiz generator using pattern matching on scraped content.
    Creates real questions from FULL article content - no API delays!
    Uses entire article text for comprehensive question generation.
    """
    import re
    
    # Use FULL text - extract key information from entire article
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    
    print(f"  - Processing {len(sentences)} sentences from full article content")
    
    if not sentences:
        return _generate_mock_quiz()
    
    # Generate comprehensive summary from full article
    # Use first few sentences + key sentences from middle
    if len(sentences) > 5:
        summary = ". ".join(sentences[:3]) + ". " + ". ".join(sentences[len(sentences)//2:len(sentences)//2+2])
        summary = summary[:500]  # Limit summary length
    else:
        summary = ". ".join(sentences[:3])[:400]
    
    if len(summary) < 50:
        summary = text[:400] + "..."
    
    # Extract entities from FULL text
    people = list(set(re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)))[:8]
    # Extract locations from entire article
    locations = list(set(re.findall(r'\b(?:the |a )?[A-Z][a-z]+(?: [A-Z][a-z]+)*\b', text)))[:15]
    locations = [l for l in locations if l.lower() not in ['the', 'a', 'an', 'this', 'that', 'these', 'those', 'and', 'or', 'but']][:8]
    
    # Generate questions from actual content
    quiz = []
    
    # Question 1: Easy - What/Who is the main subject?
    if len(sentences) > 0:
        first_sent = sentences[0]
        # Find the main subject (usually capitalized word in first sentence)
        main_subjects = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b', first_sent[:150])
        if main_subjects:
            subject = main_subjects[0]
            # Extract a short description (first 60 chars or key phrase)
            # Try to find a short descriptive phrase
            words = first_sent.split()
            short_desc = " ".join(words[:12])  # First 12 words max
            if len(short_desc) > 80:
                short_desc = short_desc[:77] + "..."
            
            # Create question with shorter options
            quiz.append({
                "question": f"Who or what is {subject}?",
                "options": [
                    short_desc if short_desc else "The main subject of this article",
                    "A fictional character",
                    "A place or location",
                    "An unrelated topic"
                ],
                "answer": short_desc if short_desc else "The main subject of this article",
                "difficulty": "easy",
                "explanation": f"This is explained in the introduction of the article."
            })
    
    # Question 2: Medium - When question (dates)
    dates = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if dates:
        year = dates[0]
        quiz.append({
            "question": "When did an important event related to this topic occur?",
            "options": [
                f"In {year}",
                f"In {int(year) + 20}",
                f"In {int(year) - 20}",
                "The date is not mentioned"
            ],
            "answer": f"In {year}",
            "difficulty": "medium",
            "explanation": f"The year {year} is mentioned in the article as significant."
        })
    
    # Question 3: Medium - Who question (people)
    if people and len(people) > 0:
        person = people[0]
        # Find short context about this person (max 60 chars)
        person_context = ""
        for sent in sentences[:10]:
            if person in sent:
                # Extract key phrase, not full sentence
                words = sent.split()
                # Find words around the person's name
                try:
                    idx = words.index(person.split()[0])
                    start = max(0, idx - 3)
                    end = min(len(words), idx + 8)
                    person_context = " ".join(words[start:end])
                    if len(person_context) > 70:
                        person_context = person_context[:67] + "..."
                except:
                    person_context = " ".join(words[:10])
                    if len(person_context) > 70:
                        person_context = person_context[:67] + "..."
                break
        
        quiz.append({
            "question": f"Who is {person}?",
            "options": [
                person_context if person_context else "A person mentioned in the article",
                "A fictional character",
                "A place name",
                "An organization"
            ],
            "answer": person_context if person_context else "A person mentioned in the article",
            "difficulty": "medium",
            "explanation": f"{person} is discussed in the article."
        })
    
    # Question 4: Hard - Key concept or detail from middle/end of article
    if len(sentences) > 5:
        # Use sentences from different parts of the article for comprehensive coverage
        mid_start = len(sentences) // 3
        mid_end = (len(sentences) * 2) // 3
        important_sentences = [s for s in sentences[mid_start:mid_end] if len(s) > 50]
        if important_sentences:
            concept_sent = important_sentences[0]
            # Extract short phrase (max 70 chars)
            words = concept_sent.split()
            short_concept = " ".join(words[:10])
            if len(short_concept) > 70:
                short_concept = short_concept[:67] + "..."
            
            quiz.append({
                "question": "What is a key detail or concept discussed in this article?",
                "options": [
                    short_concept if short_concept else "A key concept from the article",
                    "A minor detail not mentioned",
                    "An unrelated concept",
                    "Information not in the article"
                ],
                "answer": short_concept if short_concept else "A key concept from the article",
                "difficulty": "hard",
                "explanation": "This concept is discussed in detail in the article."
            })
    
    # Question 5: Medium - Extract from later in article
    if len(sentences) > 8:
        later_sentences = sentences[len(sentences)//2:]
        if later_sentences:
            later_sent = later_sentences[0]
            # Extract short phrase (max 70 chars)
            words = later_sent.split()
            short_info = " ".join(words[:10])
            if len(short_info) > 70:
                short_info = short_info[:67] + "..."
            
            quiz.append({
                "question": "What additional information is provided in this article?",
                "options": [
                    short_info if short_info else "Additional information from the article",
                    "Information not mentioned",
                    "Unrelated facts",
                    "Speculative content"
                ],
                "answer": short_info if short_info else "Additional information from the article",
                "difficulty": "medium",
                "explanation": "This information is provided in the article."
            })
    
    # Question 5: Easy - Main topic
    if len(quiz) < 5:
        # Create short summary phrase (max 70 chars)
        summary_words = summary.split()
        short_summary = " ".join(summary_words[:10])
        if len(short_summary) > 70:
            short_summary = short_summary[:67] + "..."
        
        quiz.append({
            "question": "What is the main topic of this Wikipedia article?",
            "options": [
                short_summary if short_summary else "The main topic described in the article",
                "An unrelated scientific topic",
                "A fictional story",
                "A different historical event"
            ],
            "answer": short_summary if short_summary else "The main topic described in the article",
            "difficulty": "easy",
            "explanation": "This is the main topic discussed in the article."
        })
    
    # Ensure minimum 3 questions
    while len(quiz) < 3:
        quiz.append({
            "question": "What information can you learn from this article?",
            "options": [
                "Information about the topic described",
                "Information about unrelated topics",
                "Fictional stories",
                "Scientific theories not mentioned"
            ],
            "answer": "Information about the topic described",
            "difficulty": "easy",
            "explanation": "The article provides information about its main topic."
        })
    
    return {
        "summary": summary,
        "key_entities": {
            "people": people[:5] if people else [],  # More entities from full article
            "organizations": [],
            "locations": locations[:5] if locations else []  # More locations from full article
        },
        "sections": [],
        "quiz": quiz[:7],  # Up to 7 questions from full article content
        "related_topics": []
    }

def _generate_mock_quiz():
    """Fallback mock quiz generator (only used if no content available)"""
    return {
        "summary": "This is a mock summary. Please configure GEMINI_API_KEY in your .env file to generate real quizzes.",
        "key_entities": {
            "people": ["Mock Person"],
            "organizations": ["Mock Org"],
            "locations": ["Mock Location"]
        },
        "sections": ["Introduction", "History"],
        "quiz": [
            {
                "question": "What is the mock question?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "Option A",
                "difficulty": "easy",
                "explanation": "Mock explanation."
            },
            {
                "question": "Another mock question?",
                "options": ["Choice 1", "Choice 2", "Choice 3", "Choice 4"],
                "answer": "Choice 2",
                "difficulty": "medium",
                "explanation": "Another mock explanation."
            }
        ],
        "related_topics": ["Topic 1", "Topic 2"]
    }