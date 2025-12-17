from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import logging

from src.services.rag_service import RAGService
from src.services.embedding_service import EmbeddingService
from src.services.retrieval_service import RetrievalService
from src.services.generation_service import GenerationService
from src.utils.qdrant_manager import QdrantManager
from config.settings import settings

router = APIRouter()
logger = logging.getLogger(__name__)


class ChatRequest(BaseModel):
    query: str
    context: Optional[str] = None
    language: str = "en"


class Citation(BaseModel):
    chapter_title: str
    section_heading: str
    url_anchor: str


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    language: str


# Initialize services (in a real application, these would be dependency injected)
# For this implementation, we'll initialize them directly
embedding_service = EmbeddingService()
qdrant_manager = QdrantManager()
retrieval_service = RetrievalService(embedding_service, qdrant_manager)
generation_service = GenerationService()
rag_service = RAGService(embedding_service, retrieval_service, generation_service)


@router.post("/ask", response_model=ChatResponse)
async def ask_rag_chatbot(request: ChatRequest):
    """
    Endpoint to ask a question to the RAG chatbot.
    """
    try:
        logger.info(f"Received query: {request.query[:50]}... in language: {request.language}")
        
        # Get the answer using the RAG service
        result = rag_service.get_answer(
            question=request.query,
            language=request.language,
            selected_context=request.context
        )
        
        # Format the citations from the result
        formatted_citations = [
            Citation(
                chapter_title= citation.get('chapter_title', 'Unknown Chapter'),
                section_heading=citation.get('section_heading', 'Unknown Section'),
                url_anchor=citation.get('url_anchor', '#')
            )
            for citation in result.get('citations', [])
        ]
        
        # Create the response
        response = ChatResponse(
            answer=result['answer'],
            citations=formatted_citations,
            language=result['language']
        )
        
        logger.info(f"Generated answer with {len(formatted_citations)} citations")
        return response
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@router.post("/ask-by-chapter")
async def ask_rag_by_chapter(request: ChatRequest, chapter_id: str):
    """
    Endpoint to ask a question focused on a specific chapter.
    """
    try:
        logger.info(f"Received chapter-specific query: {request.query[:50]}... for chapter: {chapter_id}")
        
        # Get the answer using the RAG service focused on a specific chapter
        result = rag_service.get_answer_by_chapter(
            question=request.query,
            chapter_id=chapter_id,
            language=request.language,
            top_k=3  # Smaller top_k for more focused results
        )
        
        # Format the citations from the result
        formatted_citations = [
            Citation(
                chapter_title= citation.get('chapter_title', 'Unknown Chapter'),
                section_heading=citation.get('section_heading', 'Unknown Section'),
                url_anchor=citation.get('url_anchor', '#')
            )
            for citation in result.get('citations', [])
        ]
        
        # Create the response
        response = ChatResponse(
            answer=result['answer'],
            citations=formatted_citations,
            language=result['language']
        )
        
        logger.info(f"Generated chapter-specific answer with {len(formatted_citations)} citations")
        return response
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error processing chapter-specific chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@router.get("/health")
async def chat_health():
    """
    Health check for the chat service.
    """
    try:
        # Test the services by creating a simple embedding
        test_text = ["health check"]
        embedding_service.encode(test_text)
        
        return {
            "status": "healthy",
            "message": "Chat service is running and able to generate embeddings"
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")


@router.post("/validate-question")
async def validate_question(request: ChatRequest):
    """
    Validate if a question is in scope of the textbook content.
    """
    try:
        # Check if the question is in scope
        is_in_scope = rag_service.check_question_in_scope(request.query)
        
        return {
            "in_scope": is_in_scope,
            "message": f"Question is {'in' if is_in_scope else 'out of'} scope"
        }
    except Exception as e:
        logger.error(f"Error validating question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error validating question: {str(e)}")