import React, { useEffect, useState } from 'react';
import api from '../api';
import QuizModal from './QuizModal';

const HistoryTable = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedQuiz, setSelectedQuiz] = useState(null);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const response = await api.get('/history');
      setQuizzes(response.data);
    } catch (err) {
      console.error('Failed to fetch history:', err);
    } finally {
      setLoading(false);
    }
  };

  const openDetails = (quiz) => {
    setSelectedQuiz(quiz);
  };

  if (loading) return <p className="loading">Loading history...</p>;

  return (
    <div className="card history-card">
      <h2 className="history-title">Past Quizzes</h2>

      {quizzes.length === 0 ? (
        <p>No quizzes generated yet.</p>
      ) : (
        <div className="table-wrapper">
          <table className="history-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Topic</th>
                <th>Summary</th>
                <th>Questions</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>
              {quizzes.map((quiz) => (
                <tr key={quiz.id}>
                  <td>{quiz.id}</td>

                  <td className="topic-cell">
                    <a
                      href={quiz.url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {quiz.title}
                    </a>
                  </td>

                  <td className="summary-cell">
                    {quiz.summary
                      ? quiz.summary.length > 120
                        ? quiz.summary.substring(0, 120) + '...'
                        : quiz.summary
                      : 'No summary'}
                  </td>

                  <td className="count-cell">
                    {quiz.quiz.length}
                  </td>

                  <td>
                    <button
                      className="details-btn"
                      onClick={() => openDetails(quiz)}
                    >
                      Details
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {selectedQuiz && (
        <QuizModal
          quiz={selectedQuiz}
          onClose={() => setSelectedQuiz(null)}
        />
      )}
    </div>
  );
};

export default HistoryTable;
