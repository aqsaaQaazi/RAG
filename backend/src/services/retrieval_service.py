from typing import List, Dict, Any, Optional
import logging
from src.services.embedding_service import EmbeddingService
from src.utils.qdrant_manager import QdrantManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RetrievalService:
    def __init__(self, embedding_service: EmbeddingService, qdrant_manager: QdrantManager):
        self.embedding_service = embedding_service
        self.qdrant_manager = qdrant_manager

    def retrieve_relevant_chunks(self, query: str, top_k: int = 5, language: str = "en") -> List[Dict[str, Any]]:
        """
        Retrieve the most relevant text chunks for a given query.
        
        Args:
            query: The user's question or query text
            top_k: Number of top results to return
            language: Language filter for results
            
        Returns:
            List of dictionaries containing relevant text chunks and metadata
        """
        try:
            # Generate embedding for the query
            query_embedding = self.embedding_service.encode_single(query)
            
            # Prepare filters for Qdrant search
            filters = {"language": language}
            
            # Search in Qdrant for similar chunks
            results = self.qdrant_manager.search_similar(
                query_embedding=query_embedding,
                top_k=top_k,
                filters=filters
            )
            
            # Format results
            relevant_chunks = []
            for result in results:
                chunk_data = {
                    "content": result.payload.get("content", ""),
                    "chapter_id": result.payload.get("chapter_id", ""),
                    "section_heading": result.payload.get("section_heading", ""),
                    "url_anchor": result.payload.get("url_anchor", ""),
                    "language": result.payload.get("language", "en"),
                    "score": result.score  # Similarity score
                }
                relevant_chunks.append(chunk_data)
            
            return relevant_chunks
        except Exception as e:
            logger.error(f"Error retrieving relevant chunks: {str(e)}")
            raise

    def retrieve_by_chapter(self, chapter_id: str, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieve relevant chunks from a specific chapter.
        
        Args:
            chapter_id: ID of the chapter to search within
            query: The user's question or query text
            top_k: Number of top results to return
            
        Returns:
            List of dictionaries containing relevant text chunks and metadata
        """
        try:
            # Generate embedding for the query
            query_embedding = self.embedding_service.encode_single(query)
            
            # Prepare filters for Qdrant search
            filters = {"chapter_id": chapter_id}
            
            # Search in Qdrant for similar chunks within the specified chapter
            results = self.qdrant_manager.search_similar(
                query_embedding=query_embedding,
                top_k=top_k,
                filters=filters
            )
            
            # Format results
            relevant_chunks = []
            for result in results:
                chunk_data = {
                    "content": result.payload.get("content", ""),
                    "chapter_id": result.payload.get("chapter_id", ""),
                    "section_heading": result.payload.get("section_heading", ""),
                    "url_anchor": result.payload.get("url_anchor", ""),
                    "language": result.payload.get("language", "en"),
                    "score": result.score  # Similarity score
                }
                relevant_chunks.append(chunk_data)
            
            return relevant_chunks
        except Exception as e:
            logger.error(f"Error retrieving chunks by chapter: {str(e)}")
            raise

    def retrieve_by_section(self, section_heading: str, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieve relevant chunks from a specific section.
        
        Args:
            section_heading: Heading of the section to search within
            query: The user's question or query text
            top_k: Number of top results to return
            
        Returns:
            List of dictionaries containing relevant text chunks and metadata
        """
        try:
            # Generate embedding for the query
            query_embedding = self.embedding_service.encode_single(query)
            
            # Prepare filters for Qdrant search
            filters = {"section_heading": section_heading}
            
            # Search in Qdrant for similar chunks within the specified section
            results = self.qdrant_manager.search_similar(
                query_embedding=query_embedding,
                top_k=top_k,
                filters=filters
            )
            
            # Format results
            relevant_chunks = []
            for result in results:
                chunk_data = {
                    "content": result.payload.get("content", ""),
                    "chapter_id": result.payload.get("chapter_id", ""),
                    "section_heading": result.payload.get("section_heading", ""),
                    "url_anchor": result.payload.get("url_anchor", ""),
                    "language": result.payload.get("language", "en"),
                    "score": result.score  # Similarity score
                }
                relevant_chunks.append(chunk_data)
            
            return relevant_chunks
        except Exception as e:
            logger.error(f"Error retrieving chunks by section: {str(e)}")
            raise

    def get_chunk_by_url_anchor(self, url_anchor: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific chunk by its URL anchor.
        
        Args:
            url_anchor: The URL anchor to search for
            
        Returns:
            Dictionary containing the text chunk and metadata, or None if not found
        """
        try:
            # This would require a direct lookup in Qdrant by the anchor
            # Since Qdrant doesn't directly support this, we use a workaround
            # by searching with a filter and taking the first result
            
            # The actual implementation would need to be done in the Qdrant manager
            # which would need to be updated to support direct anchor lookups
            logger.warning("Direct URL anchor lookup requires custom Qdrant implementation")
            return None
        except Exception as e:
            logger.error(f"Error retrieving chunk by URL anchor: {str(e)}")
            raise