[neural networks json output.json](https://github.com/user-attachments/files/24699554/neural.networks.json.output.json)[ai json output.json](https://github.com/user-attachments/files/24699540/ai.json.output.json)> 
## AI WIKI QUIZ GENERATOR
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
>Contents:
sample_data/
├── wikipedia_urls.txt
├── api_response_example_1.json
├── api_response_example_2.json
> Example Wikipedia URLs tested:
> https://en.wikipedia.org/wiki/Artificial_intelligence
> https://en.wikipedia.org/wiki/Machine_learning
> https://en.wikipedia.org/wiki/Neural_network

A `sample_data/` folder is included to demonstrate testing and API outputs.
<img width="1708" height="859" alt="Screenshot 2026-01-19 061104" src="https://github.com/user-attachments/assets/4e5ebee0-0fbb-4075-ae81-4b07e8ed3380" />
And the Json Folder contains Api outputs of tested links and Api history
neural networks json output.js{
  "id": 15,
  "url": "https://en.wikipedia.org/wiki/Neural_network",
  "title": "Neural network",
  "summary": "In biology\nIn machine learning\nHistory\nSee also\nReferences\n\nA neural network is a group of interconnected units called neurons that send signals to one another. Neurons can be either biological cells or mathematical models. While individual neurons are simple, many of them together in a network can perform complex tasks. Neurons in an artificial neural network are usually arranged into layers, with information passing from the first layer (the input layer) through one or more intermediate layers",
  "key_entities": {
    "people": [
      "Frank Rosenblatt",
      "Alexander Bain",
      "Walter Pitts",
      "Donald Hebb",
      "Horizontal Cells"
    ],
    "organizations": [],
    "locations": [
      "Populations",
      "While",
      "Walter Pitts",
      "However",
      "There"
    ]
  },
  "sections": [],
  "quiz": [
    {
      "question": "Who or what is In?",
      "options": [
        "In biology In machine learning History See also References A neural network",
        "A fictional character",
        "A place or location",
        "An unrelated topic"
      ],
      "answer": "In biology In machine learning History See also References A neural network",
      "difficulty": "easy",
      "explanation": "This is explained in the introduction of the article."
    },
    {
      "question": "When did an important event related to this topic occur?",
      "options": [
        "In 1949",
        "In 1969",
        "In 1929",
        "The date is not mentioned"
      ],
      "answer": "In 1949",
      "difficulty": "medium",
      "explanation": "The year 1949 is mentioned in the article as significant."
    },
    {
      "question": "Who is Frank Rosenblatt?",
      "options": [
        "A person mentioned in the article",
        "A fictional character",
        "A place name",
        "An organization"
      ],
      "answer": "A person mentioned in the article",
      "difficulty": "medium",
      "explanation": "Frank Rosenblatt is discussed in the article."
    },
    {
      "question": "What is a key detail or concept discussed in this article?",
      "options": [
        "[1] Populations of interconnected neurons that are smaller than neural",
        "A minor detail not mentioned",
        "An unrelated concept",
        "Information not in the article"
      ],
      "answer": "[1] Populations of interconnected neurons that are smaller than neural",
      "difficulty": "hard",
      "explanation": "This concept is discussed in detail in the article."
    },
    {
      "question": "What additional information is provided in this article?",
      "options": [
        "Neurons in an artificial neural network are usually arranged into",
        "Information not mentioned",
        "Unrelated facts",
        "Speculative content"
      ],
      "answer": "Neurons in an artificial neural network are usually arranged into",
      "difficulty": "medium",
      "explanation": "This information is provided in the article."
    }
  ],
  "related_topics": []
}
[ai json output.json](https://github.com/user-attachments/files/24699568/ai.json.output.json){
  "id": 13,
  "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
  "title": "Artificial intelligence",
  "summary": "Goals\nReasoning and problem-solving\nKnowledge representation\nPlanning and decision-making\nLearning\nNatural language processing\nPerception\nSocial intelligence\nGeneral intelligence\nTechniques\nSearch and optimization\nLogic\nProbabilistic methods for uncertain reasoning\nClassifiers and statistical learning methods\nArtificial neural networks\nDeep learning\nGPT\nHardware and software\nApplications\nHealth and medicine\nGames\nMathematics\nFinance\nMilitary\nGenerative AI\nAgents\nWeb search\nSexuality\nOther indust",
  "key_entities": {
    "people": [
      "Brian Christian",
      "Herbert Simon",
      "Marvin Minsky",
      "Lisp Machine",
      "Moritz Hardt"
    ],
    "organizations": [],
    "locations": [
      "Inference",
      "Ys",
      "Marvin Minsky",
      "Unsupervised",
      "Additionally"
    ]
  },
  "sections": [],
  "quiz": [
    {
      "question": "Who or what is Goals\nReasoning?",
      "options": [
        "Goals Reasoning and problem-solving Knowledge representation Planning and dec...",
        "A fictional character",
        "A place or location",
        "An unrelated topic"
      ],
      "answer": "Goals Reasoning and problem-solving Knowledge representation Planning and dec...",
      "difficulty": "easy",
      "explanation": "This is explained in the introduction of the article."
    },
    {
      "question": "When did an important event related to this topic occur?",
      "options": [
        "In 1956",
        "In 1976",
        "In 1936",
        "The date is not mentioned"
      ],
      "answer": "In 1956",
      "difficulty": "medium",
      "explanation": "The year 1956 is mentioned in the article as significant."
    },
    {
      "question": "Who is Brian Christian?",
      "options": [
        "A person mentioned in the article",
        "A fictional character",
        "A place name",
        "An organization"
      ],
      "answer": "A person mentioned in the article",
      "difficulty": "medium",
      "explanation": "Brian Christian is discussed in the article."
    },
    {
      "question": "What is a key detail or concept discussed in this article?",
      "options": [
        "[162][164][165][166] Generative artificial intelligence (Generative...",
        "A minor detail not mentioned",
        "An unrelated concept",
        "Information not in the article"
      ],
      "answer": "[162][164][165][166] Generative artificial intelligence (Generative...",
      "difficulty": "hard",
      "explanation": "This concept is discussed in detail in the article."
    },
    {
      "question": "What additional information is provided in this article?",
      "options": [
        "The AI learned that users tended to choose misinformation, conspiracy",
        "Information not mentioned",
        "Unrelated facts",
        "Speculative content"
      ],
      "answer": "The AI learned that users tended to choose misinformation, conspiracy",
      "difficulty": "medium",
      "explanation": "This information is provided in the article."
    }
  ],
  "related_topics": []
}
[machine larning json output.json](https://github.com/user-attachments/files/24699594/machine.larning.json.output.json){
  "id": 14,
  "url": "https://en.wikipedia.org/wiki/Machine_learning",
  "title": "Machine learning",
  "summary": "History\nRelationships to other fields\nArtificial intelligence\nData compression\nData mining\nGeneralization\nStatistics\nStatistical physics\nTheory\nApproaches\nSupervised learning\nUnsupervised learning\nSemi-supervised learning\nReinforcement learning\nOther types\nModels\nArtificial neural networks\nDecision trees\nRandom forest regression\nSupport-vector machines\nRegression analysis\nBayesian networks\nGaussian processes\nGenetic algorithms\nBelief functions\nRule-based models\nTraining models\nApplications\nLimit",
  "key_entities": {
    "people": [
      "African American",
      "Fidelity Generative",
      "Tensor Processing",
      "Racial Equality",
      "Microsoft Excel"
    ],
    "organizations": [],
    "locations": [
      "Cluster",
      "Different",
      "African American",
      "Machine",
      "the Computing Research Association"
    ]
  },
  "sections": [],
  "quiz": [
    {
      "question": "Who or what is History\nRelationships?",
      "options": [
        "History Relationships to other fields Artificial intelligence Data compressio...",
        "A fictional character",
        "A place or location",
        "An unrelated topic"
      ],
      "answer": "History Relationships to other fields Artificial intelligence Data compressio...",
      "difficulty": "easy",
      "explanation": "This is explained in the introduction of the article."
    },
    {
      "question": "When did an important event related to this topic occur?",
      "options": [
        "In 1959",
        "In 1979",
        "In 1939",
        "The date is not mentioned"
      ],
      "answer": "In 1959",
      "difficulty": "medium",
      "explanation": "The year 1959 is mentioned in the article as significant."
    },
    {
      "question": "Who is African American?",
      "options": [
        "A person mentioned in the article",
        "A fictional character",
        "A place name",
        "An organization"
      ],
      "answer": "A person mentioned in the article",
      "difficulty": "medium",
      "explanation": "African American is discussed in the article."
    },
    {
      "question": "What is a key detail or concept discussed in this article?",
      "options": [
        "Due to its generality, the field is studied in many",
        "A minor detail not mentioned",
        "An unrelated concept",
        "Information not in the article"
      ],
      "answer": "Due to its generality, the field is studied in many",
      "difficulty": "hard",
      "explanation": "This concept is discussed in detail in the article."
    },
    {
      "question": "What additional information is provided in this article?",
      "options": [
        "In addition to market basket analysis, association rules are employed",
        "Information not mentioned",
        "Unrelated facts",
        "Speculative content"
      ],
      "answer": "In addition to market basket analysis, association rules are employed",
      "difficulty": "medium",
      "explanation": "This information is provided in the article."
    }
  ],
  "related_topics": []
}




> 
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
