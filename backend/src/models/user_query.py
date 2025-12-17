from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from src.db.database import Base

if TYPE_CHECKING:
    from .chatbot_answer import ChatbotAnswer  # noqa: F401


class UserQuery(Base):
    """
    Model representing text input from the user for the RAG chatbot
    """
    __tablename__ = "user_queries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), nullable=False)  # Session identifier for conversation history
    query_text = Column(Text, nullable=False)  # The user's question
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)  # Time of the query
    language = Column(String, nullable=False, default="en")  # Language of the query
    selected_context = Column(Text, nullable=True)  # Selected text snippet from the book (optional)

    # Relationship with ChatbotAnswer
    chatbot_answer = relationship("ChatbotAnswer", back_populates="user_query", uselist=False)