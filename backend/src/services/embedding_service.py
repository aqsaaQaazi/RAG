from typing import List, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding service with a sentence transformer model.
        
        Args:
            model_name: Name of the pre-trained sentence transformer model to use
        """
        self.model_name = model_name
        try:
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {str(e)}")
            raise

    def encode(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of text strings to encode
            
        Returns:
            List of embedding vectors (each as a list of floats)
        """
        if not texts:
            return []
        
        try:
            # Generate embeddings using the sentence transformer
            embeddings = self.model.encode(texts, convert_to_numpy=True)
            
            # Convert to list of lists (needed for JSON serialization)
            embeddings_list = [embedding.tolist() for embedding in embeddings]
            
            return embeddings_list
        except Exception as e:
            logger.error(f"Error generating embeddings: {str(e)}")
            raise

    def encode_single(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.
        
        Args:
            text: Single text string to encode
            
        Returns:
            Embedding vector as a list of floats
        """
        if not text:
            return []
        
        try:
            # Generate embedding for a single text
            embedding = self.model.encode([text], convert_to_numpy=True)[0]
            return embedding.tolist()
        except Exception as e:
            logger.error(f"Error generating embedding for text: {str(e)}")
            raise

    def get_embedding_dimension(self) -> int:
        """
        Get the dimension of the embeddings produced by the model.
        
        Returns:
            Dimension of the embedding vectors
        """
        # Get a sample embedding to determine the dimension
        sample_embedding = self.model.encode(["sample text"], convert_to_numpy=True)[0]
        return len(sample_embedding)

    def cosine_similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """
        Calculate cosine similarity between two embeddings.
        
        Args:
            embedding1: First embedding vector
            embedding2: Second embedding vector
            
        Returns:
            Cosine similarity score between -1 and 1
        """
        # Convert to numpy arrays
        emb1 = np.array(embedding1)
        emb2 = np.array(embedding2)
        
        # Calculate cosine similarity
        dot_product = np.dot(emb1, emb2)
        norm1 = np.linalg.norm(emb1)
        norm2 = np.linalg.norm(emb2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        similarity = dot_product / (norm1 * norm2)
        return float(similarity)