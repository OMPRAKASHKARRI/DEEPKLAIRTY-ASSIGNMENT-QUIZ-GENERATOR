import React from 'react';

const QuizCard = ({ question, index, selectedAnswer, onAnswerSelect, showAnswers }) => {
    if (!question) return null;

    const handleOptionClick = (option) => {
        if (!showAnswers && onAnswerSelect) {
            onAnswerSelect(index, option);
        }
    };

    const isCorrect = selectedAnswer === question.answer;

    return (
        <div className="question-card">
            <h3>Question {index + 1}</h3>
            <p>{question.question}</p>

            <ul>
                {Array.isArray(question.options) &&
                    question.options.map((opt, i) => (
                        <li
                            key={i}
                            onClick={() => handleOptionClick(opt)}
                            style={{
                                cursor: showAnswers ? 'default' : 'pointer',
                                fontWeight: selectedAnswer === opt ? 'bold' : 'normal',
                                color:
                                    showAnswers && opt === question.answer
                                        ? 'green'
                                        : showAnswers && selectedAnswer === opt
                                        ? 'red'
                                        : 'black',
                            }}
                        >
                            {opt}
                        </li>
                    ))}
            </ul>

            {showAnswers && (
                <p>
                    <strong>Correct Answer:</strong> {question.answer}
                </p>
            )}
        </div>
    );
};

export default QuizCard;
