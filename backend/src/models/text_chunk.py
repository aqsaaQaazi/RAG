from typing import TYPE_CHECKING
from sqlalchemy import Column, String, Text, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
import uuid

from src.db.database import Base

if TYPE_CHECKING:
    from .chapter import Chapter  # noqa: F401
    from .textbook_content import TextbookContent  # noqa: F401


class TextChunk(Base):
    """
    Model representing segmented pieces of textbook content used for RAG ingestion and retrieval
    """
    __tablename__ = "text_chunks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id"), nullable=False)
    textbook_content_id = Column(UUID(as_uuid=True), ForeignKey("textbook_content.id"), nullable=False)
    content = Column(Text, nullable=False)
    
    # Embedding as an array of floats (will be populated after processing)
    embedding = Column(ARRAY(Float), nullable=True)
    
    section_heading = Column(String, nullable=True)
    url_anchor = Column(String, nullable=True)
    language = Column(String, nullable=False, default="en")

    # Relationships
    chapter = relationship("Chapter", back_populates="text_chunks")
    textbook_content = relationship("TextbookContent", back_populates="text_chunks")