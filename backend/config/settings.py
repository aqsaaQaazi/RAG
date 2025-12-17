import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Qdrant settings
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_API_KEY: str | None = os.getenv("QDRANT_API_KEY")
    
    # Neon PostgreSQL settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    
    # Google Cloud Vertex AI settings
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID", "")
    VERTEX_AI_EMBEDDING_MODEL: str = os.getenv("VERTEX_AI_EMBEDDING_MODEL", "text-embedding-004")
    GEMINI_MODEL_NAME: str = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash-001")
    
    # Application settings
    APP_NAME: str = "RAG Textbook API"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # RAG settings
    RAG_TEMPERATURE: float = float(os.getenv("RAG_TEMPERATURE", "0.2"))
    RAG_MAX_TOKENS: int = int(os.getenv("RAG_MAX_TOKENS", "500"))
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "100"))
    
    # Frontend URL for CORS
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    class Config:
        env_file = ".env"

settings = Settings()