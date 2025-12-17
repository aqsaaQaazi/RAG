from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
import os

from src.services.ingestion_service import IngestionService

router = APIRouter()


class IngestionRequest(BaseModel):
    directory_path: str
    chunk_size: Optional[int] = 1000
    overlap: Optional[int] = 100
    language: Optional[str] = "en"


class IngestionResponse(BaseModel):
    success: bool
    message: str
    files_processed: int


@router.post("/ingest", response_model=IngestionResponse)
async def ingest_content(request: IngestionRequest):
    """
    Ingest textbook content from a directory of markdown files.
    """
    try:
        # Validate the directory exists
        if not os.path.exists(request.directory_path):
            raise HTTPException(status_code=400, detail="Directory does not exist")
        
        if not os.path.isdir(request.directory_path):
            raise HTTPException(status_code=400, detail="Path is not a directory")
        
        # Initialize the ingestion service
        ingestion_service = IngestionService()
        
        # Perform ingestion
        success = ingestion_service.ingest_textbook(request.directory_path)
        
        if success:
            # Count the number of markdown files in the directory
            md_files = list(Path(request.directory_path).glob("*.md"))
            return IngestionResponse(
                success=True,
                message=f"Successfully ingested {len(md_files)} files",
                files_processed=len(md_files)
            )
        else:
            return IngestionResponse(
                success=False,
                message="Ingestion failed",
                files_processed=0
            )
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")


@router.post("/ingest-file")
async def ingest_single_file(file_path: str):
    """
    Ingest a single markdown file.
    """
    try:
        if not os.path.exists(file_path):
            raise HTTPException(status_code=400, detail="File does not exist")
        
        if not file_path.endswith('.md'):
            raise HTTPException(status_code=400, detail="File must be a markdown file (.md)")
        
        # Initialize the ingestion service
        ingestion_service = IngestionService()
        
        # Process the single file
        result = ingestion_service.process_textbook_content(file_path)
        
        # Add the content to Qdrant
        success = ingestion_service.qdrant_manager.add_texts_with_embeddings(
            result['content_chunks'],
            result['chunk_metadata']
        )
        
        if success:
            return {"success": True, "message": f"Successfully ingested file: {file_path}"}
        else:
            return {"success": False, "message": "Failed to add content to Qdrant"}
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File ingestion failed: {str(e)}")


@router.get("/status")
async def ingestion_status():
    """
    Get the status of the ingestion service.
    """
    try:
        # Initialize the ingestion service to test connection
        ingestion_service = IngestionService()
        
        # Test Qdrant connection
        # In a real implementation, we would check the actual connection status
        # For now, we'll just return that the service is available
        return {
            "status": "available",
            "qdrant_connection": "assumed_connected",  # In a real implementation, test actual connection
            "message": "Ingestion service is running"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Service status check failed: {str(e)}")