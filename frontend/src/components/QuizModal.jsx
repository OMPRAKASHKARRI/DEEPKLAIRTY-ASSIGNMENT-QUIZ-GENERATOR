import React, { useState } from 'react';
import QuizCard from './QuizCard';

const QuizModal = ({ quiz, onClose }) => {
    const [selectedAnswers, setSelectedAnswers] = useState({});
    const [showAnswers, setShowAnswers] = useState(false);

    if (!quiz) return null;

    const handleAnswerSelect = (questionIndex, answer) => {
        setSelectedAnswers(prev => ({
            ...prev,
            [questionIndex]: answer
        }));
    };

    const handleSubmit = () => {
        setShowAnswers(true);
    };

    const handleReset = () => {
        setSelectedAnswers({});
        setShowAnswers(false);
    };

    return (
        <div className="modal-overlay" onClick={onClose}>
            <div className="modal-content" onClick={e => e.stopPropagation()}>
                <button className="close-btn" onClick={onClose}>&times;</button>

                <div className="quiz-header">
                    <h2>{quiz.title}</h2>
                    <p>{quiz.summary}</p>
                </div>

                {Array.isArray(quiz.quiz) && quiz.quiz.map((q, i) => (
                    <QuizCard
                        key={i}
                        question={q}
                        index={i}
                        selectedAnswer={selectedAnswers[i] || null}
                        onAnswerSelect={handleAnswerSelect}
                        showAnswers={showAnswers}
                    />
                ))}

                <div className="card" style={{ marginTop: '1rem', textAlign: 'center' }}>
                    {!showAnswers ? (
                        <button onClick={handleSubmit}>Submit Quiz</button>
                    ) : (
                        <button onClick={handleReset}>Retake Quiz</button>
                    )}
                </div>
            </div>
        </div>
    );
};

export default QuizModal;
