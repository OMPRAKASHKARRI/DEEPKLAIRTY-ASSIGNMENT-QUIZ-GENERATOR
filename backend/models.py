from sqlalchemy import Column, Integer, String, JSON, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=False, index=True)
    title = Column(String)
    summary = Column(Text)
    key_entities = Column(JSON)  # Stores people, organizations, locations
    related_topics = Column(JSON) # List of strings
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    question_text = Column(Text)
    options = Column(JSON) # List of strings [A, B, C, D]
    answer = Column(String)
    difficulty = Column(String)
    explanation = Column(Text)

    quiz = relationship("Quiz", back_populates="questions")