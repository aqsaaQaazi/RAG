from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from src.db.database import Base


class LanguagePreference(Base):
    """
    Model representing user's chosen language for the textbook and chatbot
    """
    __tablename__ = "language_preferences"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Identifier for the user
    preferred_language = Column(String, nullable=False)  # ISO 639-1 code for the preferred language