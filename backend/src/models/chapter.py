from typing import TYPE_CHECKING, List
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from src.db.database import Base

if TYPE_CHECKING:
    from .textbook_content import TextbookContent  # noqa: F401
    from .text_chunk import TextChunk  # noqa: F401
    from .source_citation import SourceCitation  # noqa: F401


class Chapter(Base):
    """
    Model representing a discrete section of the textbook
    """
    __tablename__ = "chapters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    textbook_content_id = Column(UUID(as_uuid=True), ForeignKey("textbook_content.id"), nullable=False)
    title = Column(String, nullable=False)
    order = Column(Integer, nullable=False)  # Chapter order in the textbook
    slug = Column(String, nullable=False)  # URL-friendly identifier
    content_summary = Column(Text, nullable=True)  # Brief summary
    key_ideas = Column(Text, nullable=True)  # List of key ideas
    practical_checklist = Column(Text, nullable=True)  # List of practical checklist items

    # Relationship with TextbookContent
    textbook_content = relationship("TextbookContent", back_populates="chapters")
    
    # Relationship with TextChunk
    text_chunks = relationship("TextChunk", back_populates="chapter")

    # Relationship with SourceCitation
    citations = relationship("SourceCitation", back_populates="chapter")