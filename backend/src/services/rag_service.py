import logging
from typing import List, Dict, Any, Optional
from src.services.embedding_service import EmbeddingService
from src.services.retrieval_service import RetrievalService
from src.services.generation_service import GenerationService
from src.utils.qdrant_manager import QdrantManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGService:
    def __init__(self, 
                 embedding_service: EmbeddingService, 
                 retrieval_service: RetrievalService, 
                 generation_service: GenerationService):
        self.embedding_service = embedding_service
        self.retrieval_service = retrieval_service
        self.generation_service = generation_service

    def get_answer(self, 
                   question: str, 
                   language: str = "en", 
                   selected_context: Optional[str] = None,
                   top_k: int = 5) -> Dict[str, Any]:
        """
        Main RAG method to get an answer to a question based on textbook content.
        
        Args:
            question: The user's question
            language: The language for the response
            selected_context: Optional additional context selected by the user
            top_k: Number of relevant chunks to retrieve
            
        Returns:
            Dictionary containing the answer and citations
        """
        try:
            # Step 1: Retrieve relevant chunks based on the question
            relevant_chunks = self.retrieval_service.retrieve_relevant_chunks(
                query=question,
                top_k=top_k,
                language=language
            )
            
            # Step 2: Generate the answer based on the retrieved chunks and question
            if selected_context:
                result = self.generation_service.generate_answer_with_selected_context(
                    question=question,
                    selected_context=selected_context,
                    context_chunks=relevant_chunks,
                    language=language
                )
            else:
                result = self.generation_service.generate_answer(
                    question=question,
                    context_chunks=relevant_chunks,
                    language=language
                )
            
            # Step 3: Validate the answer if needed (optional)
            is_relevant = self.generation_service.validate_answer_relevance(question, result['answer'])
            if not is_relevant:
                logger.warning(f"Generated answer may not be fully relevant to question: {question}")
            
            return result
        except Exception as e:
            logger.error(f"Error in RAG service: {str(e)}")
            raise

    def get_answer_by_chapter(self, 
                              question: str, 
                              chapter_id: str, 
                              language: str = "en",
                              top_k: int = 3) -> Dict[str, Any]:
        """
        Get an answer to a question focused on a specific chapter.
        
        Args:
            question: The user's question
            chapter_id: ID of the chapter to focus on
            language: The language for the response
            top_k: Number of relevant chunks to retrieve
            
        Returns:
            Dictionary containing the answer and citations
        """
        try:
            # Step 1: Retrieve relevant chunks within the specified chapter
            relevant_chunks = self.retrieval_service.retrieve_by_chapter(
                chapter_id=chapter_id,
                query=question,
                top_k=top_k
            )
            
            # Step 2: Generate the answer based on the retrieved chunks and question
            result = self.generation_service.generate_answer(
                question=question,
                context_chunks=relevant_chunks,
                language=language
            )
            
            # Step 3: Validate the answer if needed (optional)
            is_relevant = self.generation_service.validate_answer_relevance(question, result['answer'])
            if not is_relevant:
                logger.warning(f"Generated answer may not be fully relevant to question: {question}")
            
            return result
        except Exception as e:
            logger.error(f"Error in chapter-specific RAG service: {str(e)}")
            raise

    def get_answer_by_section(self, 
                              question: str, 
                              section_heading: str, 
                              language: str = "en",
                              top_k: int = 3) -> Dict[str, Any]:
        """
        Get an answer to a question focused on a specific section.
        
        Args:
            question: The user's question
            section_heading: Heading of the section to focus on
            language: The language for the response
            top_k: Number of relevant chunks to retrieve
            
        Returns:
            Dictionary containing the answer and citations
        """
        try:
            # Step 1: Retrieve relevant chunks within the specified section
            relevant_chunks = self.retrieval_service.retrieve_by_section(
                section_heading=section_heading,
                query=question,
                top_k=top_k
            )
            
            # Step 2: Generate the answer based on the retrieved chunks and question
            result = self.generation_service.generate_answer(
                question=question,
                context_chunks=relevant_chunks,
                language=language
            )
            
            # Step 3: Validate the answer if needed (optional)
            is_relevant = self.generation_service.validate_answer_relevance(question, result['answer'])
            if not is_relevant:
                logger.warning(f"Generated answer may not be fully relevant to question: {question}")
            
            return result
        except Exception as e:
            logger.error(f"Error in section-specific RAG service: {str(e)}")
            raise

    def check_question_in_scope(self, question: str) -> bool:
        """
        Check if a question is within the scope of the textbook content.
        
        Args:
            question: The question to check
            
        Returns:
            Boolean indicating if the question is in scope
        """
        try:
            # This is a simplified check - in a more advanced implementation,
            # we might use semantic similarity or topic modeling
            out_of_scope_keywords = [
                "unrelated topic", "different book", "another subject",
                "not in textbook", "not mentioned in book"
            ]
            
            question_lower = question.lower()
            for keyword in out_of_scope_keywords:
                if keyword in question_lower:
                    return False
            
            # For now, we'll assume most questions are in scope and let the retrieval
            # step determine if we can find relevant content
            return True
        except Exception as e:
            logger.error(f"Error checking question scope: {str(e)}")
            # Default to True to be safe
            return True

    def get_fallback_response(self, question: str, language: str = "en") -> Dict[str, Any]:
        """
        Generate a fallback response when no relevant content is found.
        
        Args:
            question: The original question
            language: The language for the response
            
        Returns:
            Dictionary containing the fallback answer and empty citations
        """
        fallback_answer = (
            "I cannot find an answer to this question in the textbook. "
            "The information you're looking for may not be covered in the Physical AI & "
            "Humanoid Robotics textbook, or it might be phrased differently than in the source material."
        )
        
        return {
            "answer": fallback_answer,
            "citations": [],
            "language": language
        }