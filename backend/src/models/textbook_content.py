from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from src.db.database import Base

if TYPE_CHECKING:
    from .chapter import Chapter  # noqa: F401


class TextbookContent(Base):
    """
    Model representing raw textbook content (Markdown/MDX files, diagrams, code snippets)
    """
    __tablename__ = "textbook_content"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    language = Column(String, nullable=False, default="en")
    last_modified = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationship with Chapter
    chapters = relationship("Chapter", back_populates="textbook_content")