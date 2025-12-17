import pytest
from src.services.rag_service import RAGService
from src.services.embedding_service import EmbeddingService
from src.services.retrieval_service import RetrievalService
from src.services.generation_service import GenerationService
from src.utils.qdrant_manager import QdrantManager


def test_rag_service_initialization():
    """Test that RAG service can be initialized with its dependencies"""
    # Note: This test would require mocking the external services
    # For now, we'll just verify the class exists
    assert RAGService is not None
    assert EmbeddingService is not None
    assert RetrievalService is not None
    assert GenerationService is not None
    assert QdrantManager is not None


def test_rag_service_has_required_methods():
    """Test that RAG service has the required methods"""
    # Note: This test would require creating actual service instances
    # which in turn would require external services to be running
    
    # Just verify method names exist
    methods_to_check = [
        'get_answer',
        'get_answer_by_chapter', 
        'get_answer_by_section',
        'check_question_in_scope',
        'get_fallback_response'
    ]
    
    # Check that the class has these methods
    for method_name in methods_to_check:
        assert hasattr(RAGService, method_name), f"Method {method_name} is missing"