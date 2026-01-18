> # Quiz App
>
> **A full-stack web application that generates interactive quizzes from Wikipedia articles using AI-powered content analysis.**  
> Built with a **FastAPI backend** and a **React frontend**.
>
> ---
>
> ## 🚀 Features
>
> - AI-powered quiz generation from any Wikipedia article  
> - Interactive quiz interface with real-time feedback  
> - Quiz history with retake support  
> - Responsive, mobile-friendly UI  
> - High-performance FastAPI backend  
> - SQLite database for persistent storage  
> - Loading indicators during AI processing  
>
> ---
> ## 🖼 Screenshots



- **Quiz Generation Page (Tab 1)**  
  <img width="1920" height="1080" alt="Screenshot 2026-01-18 083350" src="https://github.com/user-attachments/assets/0c56a012-1ad3-4095-9050-a23bc174bdad" />

- **History View (Tab 2)**  
  <img width="1920" height="1080" alt="Screenshot 2026-01-18 083421" src="https://github.com/user-attachments/assets/b3da985e-0d57-4479-baed-38654bd3cd6e" />


- **Quiz Details Modal**  
  <img width="1920" height="1080" alt="Screenshot 2026-01-18 083433" src="https://github.com/user-attachments/assets/d88fc33f-7068-41ff-b605-7155fe70f18a" />

>
>## 🧪 Sample Data

A `sample_data/` folder is included to demonstrate testing and API outputs.

Contents:
sample_data/
├── wikipedia_urls.txt
├── api_response_example_1.json
├── api_response_example_2.json
> Example Wikipedia URLs tested:
> https://en.wikipedia.org/wiki/Artificial_intelligence
> https://en.wikipedia.org/wiki/Machine_learning
> https://en.wikipedia.org/wiki/Neural_network
 The JSON files contain actual API responses returned by the quiz generation endpoint, showing quiz structure, questions, options, answers, and related topics.

> ## 🛠 Tech Stack
>
> **Backend**
> - FastAPI (Python)
> - SQLite + SQLAlchemy (Async)
> - Google Generative AI
> - BeautifulSoup4 + Requests
> - Uvicorn
>
> **Frontend**
> - Framework: React 19
> - Build Tool: Vite
> - HTTP Client: Axios
> - Styling: CSS Modules
> - ASGI Server: Uvicorn
>
> ---
>
> ## 📋 Prerequisites
>
> - Python 3.8+
> - Node.js 16+
> - Google AI API Key
>
> ---
> ## 🔗 API Endpoints

The backend exposes the following REST API endpoints:

- `GET /api/health` – Health check
- `POST /api/generate` – Generate quiz from Wikipedia URL
- `GET /api/history` – Fetch quiz history
- `GET /api/history/{id}` – Fetch full quiz details by ID

Live API documentation is available at:
https://deepklairty-assignment-quiz-generator.onrender.com/docs
> ## Sample Output Structure
>{
  "id": 1,
  "url": "[https://en.wikipedia.org/wiki/Alan_Turing](https://en.wikipedia.org/wiki/Alan_Turing)",
  "title": "Alan Turing",
  "summary": "Alan Turing was a British mathematician and computer scientist...",
  "key_entities": {
    "people": ["Alan Turing", "Alonzo Church"],
    "organizations": ["University of Cambridge", "Bletchley Park"],
    "locations": ["United Kingdom"]
  },
  "sections": ["Early life", "World War II", "Legacy"],
  "quiz": [
    {
      "question": "Where did Alan Turing study?",
      "options": [
        "Harvard University",
        "Cambridge University",
        "Oxford University",
        "Princeton University"
      ],
      "answer": "Cambridge University",
      "difficulty": "easy",
      "explanation": "Mentioned in the 'Early life' section."
    },
    {
      "question": "What was Alan Turing's main contribution during World War II?",
      "options": [
        "Atomic research",
        "Breaking the Enigma code",
        "Inventing radar",
        "Developing jet engines"
      ],
      "answer": "Breaking the Enigma code",
      "difficulty": "medium",
      "explanation": "Detailed in the 'World War II' section."
    }
  ],
  "related_topics": ["Cryptography", "Enigma machine", "Computer science history"]
}

> ## ⚙️ Installation
>
> **Clone Repository**
> ```bash
> git clone <repository-url>
> cd quiz_app
> ```
>
> **Backend Setup**
> ```bash
> cd backend
> python -m venv venv
> venv\Scripts\activate   # Windows
> source venv/bin/activate # macOS/Linux
> pip install -r requirements.txt
> ```
>
> Create `.env` file:
> ```env
> GOOGLE_API_KEY=your_google_ai_api_key_here
> ```
>
> **Frontend Setup**
> ```bash
> cd ../frontend
> npm install
> ```
>
> ---
>
> ## ▶️ Running the App
>
> **Backend**
> ```bash
> uvicorn main:app --reload
> ```
> API: https://deepklairty-assignment-quiz-generator.onrender.com/API  
> Docs: https://deepklairty-assignment-quiz-generator.onrender.com/docs
>
> **Frontend**
> ```bash
> npm run dev
> ```
> App: https://deepklairty-assignment-quiz-generat.vercel.app/
>
> ---
>## LangChain Prompt Templates

The following prompt templates were used for quiz and related-topic generation.

Quiz generation prompt:
You are an AI assistant that creates multiple-choice quizzes.

Given the following Wikipedia article content:
{article_text}

Generate 5 multiple-choice questions.
Each question must have 4 options, one correct answer,
and a short explanation.

Return the result in structured JSON format.
Based on the following Wikipedia article content:
{article_text}

Generate a list of 5 related topics a learner should explore next.
Return the result as a JSON array of strings.
> ## 🧪 How to Use
>
> 1. Open https://deepklairty-assignment-quiz-generat.vercel.app/
> 2. Enter a Wikipedia URL  
> 3. Click **Generate Quiz**  
> 4. Answer questions and submit  
> 5. View score and explanations  
> 6. Check **History** for past quizzes  
>
> ---
>
> ## 📁 Project Structure
>
> ```text
> kalrity2/
> ├── backend/
> │   ├── main.py
> │   ├── database.py
> │   ├── models.py
> │   ├── services.py
> │   ├── requirements.txt
> │   └── quiz_app.db
> ├── frontend/
> │   ├── src/
> │   │   ├── api.js
> │   │   ├── App.jsx
> │   │   ├── App.css
> │   │   ├── index.css
> │   │   └── components/
> │   └── vite.config.js
> └── README.md
> ```
>
> ---
>
> ## 🔗 API Endpoints
>
> - `GET /api/health` – Health check  
> - `POST /api/generate` – Generate quiz  
> - `GET /api/history` – Quiz history  
> - `GET /api/history/{id}` – Quiz details  
>
> ---
>
> ## 🗄 Database
>
> **Quiz Table**
> - id, url, title, summary, key_entities, related_topics, created_at
>
> **Question Table**
> - id, quiz_id, question_text, options, answer, difficulty, explanation
>
> ---
>
> ## 📦 Production Build
>
> **Backend**
> ```bash
> gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
> ```
>
> **Frontend**
> ```bash
> npm run build
> ```
>
> ---
>
> ## 🏢 About
>
> **DeepKlarity Technologies – AI Wiki Quiz Generator Assignment**
>
> ---
>
> ## 📄 License
>
> MIT License
