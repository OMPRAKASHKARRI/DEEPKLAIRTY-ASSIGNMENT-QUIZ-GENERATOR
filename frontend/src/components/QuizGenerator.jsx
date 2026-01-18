import React, { useState } from 'react';
import api from '../api';

const QuizGenerator = () => {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [loadingStep, setLoadingStep] = useState('');
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [showAnswers, setShowAnswers] = useState(false);

  const handleAnswerSelect = (qIndex, answer) => {
    if (showAnswers) return;

    setSelectedAnswers((prev) => ({
      ...prev,
      [qIndex]: answer,
    }));
  };

  const handleSubmit = () => {
    setShowAnswers(true);
  };

  const handleReset = () => {
    setSelectedAnswers({});
    setShowAnswers(false);
  };

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!url) return;

    setLoading(true);
    setError(null);
    setResult(null);
    setSelectedAnswers({});
    setShowAnswers(false);
    setLoadingStep('Scraping article content...');

    try {
      const progressTimer = setTimeout(() => {
        setLoadingStep('Generating quiz with AI...');
      }, 2000);

      const response = await api.post(
        'http://127.0.0.1:8000/api/generate',
        { url }
      );

      clearTimeout(progressTimer);
      setLoadingStep('');
      setResult(response.data);
    } catch (err) {
      setLoadingStep('');
      setError(
        err.response?.data?.detail ||
          'Failed to generate quiz. Please check the URL.'
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {/* Generate Quiz */}
      <div className="card">
        <h2>Generate New Quiz</h2>

        <form onSubmit={handleGenerate}>
          <input
            type="url"
            placeholder="Enter Wikipedia Article URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Generating…' : 'Generate Quiz'}
          </button>
        </form>

        {loading && <p className="loading">{loadingStep}</p>}
        {error && <p className="error">{error}</p>}
      </div>

      {/* Quiz Questions */}
      {result && (
        <div className="card quiz-container">
          <h2 className="quiz-title">{result.title}</h2>
          <p className="quiz-summary">{result.summary}</p>

          {result.quiz.map((q, i) => (
            <div key={i} className="question-block">
              <h3 style={{ color: '#111827' }}>
                Question {i + 1}
              </h3>
              <p style={{ marginBottom: '1rem', color: '#374151' }}>
                {q.question}
              </p>

              {q.options.map((opt, idx) => {
                const isCorrect =
                  showAnswers && opt === q.answer;
                const isWrong =
                  showAnswers &&
                  selectedAnswers[i] === opt &&
                  opt !== q.answer;

                return (
                  <div
  key={idx}
  className={`option
    ${selectedAnswers[i] === opt ? 'selected' : ''}
    ${isCorrect ? 'correct' : ''}
    ${isWrong ? 'wrong' : ''}
  `}
  style={{ color: '#111827' }}
  onClick={() => handleAnswerSelect(i, opt)}
>
  {opt}
</div>

);
              })}
            </div>
          ))}

          {/* Submit / Score */}
          <div className="submit-area">
            {!showAnswers ? (
              <button
                className="submit-btn"
                onClick={handleSubmit}
              >
                Submit Quiz
              </button>
            ) : (
              <>
                <p className="score-box">
                  Score:{' '}
                  {
                    Object.keys(selectedAnswers).filter(
                      (i) =>
                        selectedAnswers[i] ===
                        result.quiz[i]?.answer
                    ).length
                  }
                  / {result.quiz.length}
                </p>

                <button
                  className="submit-btn"
                  onClick={handleReset}
                >
                  Retake Quiz
                </button>
              </>
            )}
          </div>
        </div>
      )}
    </>
  );
};

export default QuizGenerator;
