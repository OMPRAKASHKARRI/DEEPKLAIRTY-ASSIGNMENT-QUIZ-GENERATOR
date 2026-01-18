# Quiz App Backend

A FastAPI-based backend service for generating interactive quizzes from Wikipedia articles using AI-powered content analysis.

## Features

- **AI-Powered Quiz Generation**: Automatically generates multiple-choice questions from Wikipedia articles using Google Generative AI
- **Fast Content Scraping**: Efficiently scrapes and processes Wikipedia content with timeout handling
- **Database Storage**: Stores generated quizzes and questions in SQLite database with async SQLAlchemy
- **RESTful API**: Clean REST endpoints for quiz generation and history management
- **CORS Support**: Configured for frontend integration
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **Health Check**: Built-in health check endpoint for monitoring

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy (async)
- **AI Service**: Google Generative AI
- **Web Scraping**: BeautifulSoup4 + Requests
- **ASGI Server**: Uvicorn
- **Data Validation**: Pydantic

## Prerequisites

- Python 3.8+
- Google AI API Key (for quiz generation)

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd quiz_app/backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the backend directory:
   ```
   GOOGLE_API_KEY=your_google_ai_api_key_here
   ```

## Usage

1. **Start the server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**:
   Open your browser and go to `http://localhost:8000/docs` for interactive Swagger UI documentation.

## API Endpoints

### Health Check
- **GET** `/api/health`
- Returns server status

### Generate Quiz
- **POST** `/api/generate`
- Request body: `{"url": "https://en.wikipedia.org/wiki/Example"}`
- Generates and returns a quiz from the provided Wikipedia URL

### Get Quiz History
- **GET** `/api/history`
- Returns a list of all generated quizzes

### Get Quiz Details
- **GET** `/api/history/{id}`
- Returns detailed information for a specific quiz by ID

## Project Structure

```
backend/
├── main.py          # FastAPI application and endpoints
├── models.py        # SQLAlchemy database models
├── database.py      # Database configuration and session management
├── services.py      # Business logic for scraping and AI generation
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Database Schema

### Quiz Table
- `id`: Primary key
- `url`: Source Wikipedia URL
- `title`: Article title
- `summary`: AI-generated summary
- `key_entities`: JSON object with extracted entities
- `related_topics`: JSON array of related topics
- `created_at`: Timestamp

### Question Table
- `id`: Primary key
- `quiz_id`: Foreign key to Quiz
- `question_text`: Question content
- `options`: JSON array of answer options
- `answer`: Correct answer
- `difficulty`: Question difficulty level
- `explanation`: Answer explanation

## Configuration

The application uses the following configuration:
- **Database**: SQLite database file `quiz.db`
- **AI Timeout**: 8 seconds total for quiz generation
- **Scraping Timeout**: 6 seconds for web scraping
- **CORS**: Allows all origins for development (configure for production)

## Error Handling

The API includes comprehensive error handling:
- 400: Bad Request (invalid URL, scraping failed)
- 404: Not Found (quiz not found)
- 408: Request Timeout (scraping timeout)
- 500: Internal Server Error (AI generation failed)
- 504: Gateway Timeout (overall request timeout)

## Development

### Running Tests
```bash
# Add test commands here when implemented
```

### Code Formatting
```bash
# Add linting/formatting commands here when configured
```

## Deployment

1. Set environment variables in production
2. Use a production ASGI server like Gunicorn with Uvicorn workers
3. Configure CORS origins for your frontend domain
4. Set up proper logging and monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.