from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from config.settings import settings

# Create the database engine
engine = create_engine(
    settings.DATABASE_URL,
    # For SQLite only - remove for PostgreSQL
    # connect_args={"check_same_thread": False},
    # poolclass=StaticPool  # Uncomment for SQLite in testing
)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()