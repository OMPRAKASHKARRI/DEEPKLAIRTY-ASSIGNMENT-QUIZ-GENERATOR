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
>
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
>
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
> API: http://localhost:8000  
> Docs: http://localhost:8000/docs
>
> **Frontend**
> ```bash
> npm run dev
> ```
> App: http://localhost:5173
>
> ---
>
> ## 🧪 How to Use
>
> 1. Open http://localhost:5173  
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
