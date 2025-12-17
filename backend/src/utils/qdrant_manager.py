import qdrant_client
from qdrant_client.http import models
from typing import List, Dict, Any
from config.settings import settings


class QdrantManager:
    def __init__(self):
        # Initialize Qdrant client
        self.client = qdrant_client.QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            prefer_grpc=False  # Using REST API instead of gRPC
        )
        
        # Define collection name for text chunks
        self.collection_name = "textbook_chunks"
    
    def create_collection(self):
        """Create the collection for storing textbook content embeddings"""
        try:
            # Check if collection already exists
            collections = self.client.get_collections()
            collection_names = [col.name for col in collections.collections]
            
            if self.collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=models.VectorParams(
                        size=768,  # Default size for sentence transformer embeddings
                        distance=models.Distance.COSINE
                    )
                )
                
                # Create payload index for faster filtering
                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="chapter_id",
                    field_schema=models.PayloadSchemaType.KEYWORD
                )
                
                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="language",
                    field_schema=models.PayloadSchemaType.KEYWORD
                )
        except Exception as e:
            print(f"Error creating Qdrant collection: {e}")
            raise
    
    def add_texts_with_embeddings(self, texts: List[str], metadatas: List[Dict[str, Any]]):
        """Add texts with their embeddings to the Qdrant collection"""
        try:
            # This would require an embedding model to generate vectors
            # For now, we'll outline the structure
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight model
            embeddings = model.encode(texts)
            
            points = []
            for i, (text, embedding, metadata) in enumerate(zip(texts, embeddings, metadatas)):
                points.append(
                    models.PointStruct(
                        id=i,
                        vector=embedding.tolist(),
                        payload={
                            "content": text,
                            "chapter_id": metadata.get("chapter_id"),
                            "section_heading": metadata.get("section_heading"),
                            "url_anchor": metadata.get("url_anchor"),
                            "language": metadata.get("language", "en"),
                        }
                    )
                )
            
            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            
            return True
        except Exception as e:
            print(f"Error adding texts to Qdrant: {e}")
            return False
    
    def search_similar(self, query_embedding: List[float], top_k: int = 5, filters: Dict = None):
        """Search for similar text chunks based on embedding similarity"""
        try:
            if filters is None:
                filters = {}
            
            search_filter = None
            if filters:
                filter_conditions = []
                for key, value in filters.items():
                    filter_conditions.append(
                        models.FieldCondition(
                            key=key,
                            match=models.MatchValue(value=value)
                        )
                    )
                
                if filter_conditions:
                    search_filter = models.Filter(
                        must=filter_conditions
                    )
            
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=top_k,
                query_filter=search_filter
            )
            
            return results
        except Exception as e:
            print(f"Error searching in Qdrant: {e}")
            return []