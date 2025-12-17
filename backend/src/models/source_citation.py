from typing import TYPE_CHECKING
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from src.db.database import Base

if TYPE_CHECKING:
    from .chatbot_answer import ChatbotAnswer  # noqa: F401
    from .chapter import Chapter  # noqa: F401


class SourceCitation(Base):
    """
    Model representing references to specific parts of the textbook supporting a chatbot answer
    """
    __tablename__ = "source_citations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chatbot_answer_id = Column(UUID(as_uuid=True), ForeignKey("chatbot_answers.id"), nullable=False)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id"), nullable=False)
    section_heading = Column(String, nullable=False)  # Heading of the cited section
    url_anchor = Column(String, nullable=False)  # URL anchor for direct linking

    # Relationship with ChatbotAnswer
    chatbot_answer = relationship("ChatbotAnswer", back_populates="citations")
    
    # Relationship with Chapter
    chapter = relationship("Chapter", back_populates="citations")