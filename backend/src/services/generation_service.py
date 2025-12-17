import logging
from typing import List, Dict, Any
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_google_vertexai import ChatVertexAI
from langchain.chains import LLMChain
from config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SourceCitation(BaseModel):
    chapter_title: str = Field(description="Title of the chapter where the information is found")
    section_heading: str = Field(description="Heading of the section within the chapter")
    url_anchor: str = Field(description="URL anchor for direct linking to the specific section")


class GenerationService:
    def __init__(self):
        # Initialize the LLM with configuration from settings
        self.llm = ChatVertexAI(
            model_name=settings.GEMINI_MODEL_NAME,
            project=settings.GCP_PROJECT_ID,
            temperature=settings.RAG_TEMPERATURE,
            max_output_tokens=settings.RAG_MAX_TOKENS
        )
        
        # Define the prompt template for RAG
        self.rag_prompt = PromptTemplate(
            input_variables=["context", "question", "language"],
            template="""
            You are an expert assistant for the Physical AI & Humanoid Robotics textbook.
            Answer the question based only on the provided context from the textbook.
            If the answer is not available in the context, clearly state that the answer is not found in the book.
            
            Context: {context}
            
            Question: {question}
            
            Language: {language}
            
            Provide a clear, concise, and helpful answer based only on the textbook content.
            If the answer is not in the textbook, respond with: "I cannot find an answer to this question in the textbook."
            
            If you can answer, also provide citations to the textbook sections that support your answer.
            """
        )
        
        # Create the LLM chain
        self.rag_chain = LLMChain(llm=self.llm, prompt=self.rag_prompt)

    def generate_answer(self, question: str, context_chunks: List[Dict[str, Any]], language: str = "en") -> Dict[str, Any]:
        """
        Generate an answer to the question based on the provided context chunks.
        
        Args:
            question: The user's question
            context_chunks: List of context chunks retrieved from the textbook
            language: The language for the response
            
        Returns:
            Dictionary containing the answer and citations
        """
        try:
            # Combine the context chunks into a single context string
            context_texts = [chunk['content'] for chunk in context_chunks if chunk.get('content')]
            combined_context = "\n\n".join(context_texts)
            
            if not combined_context.strip():
                # If no context was found, return appropriate response
                return {
                    "answer": "I cannot find an answer to this question in the textbook.",
                    "citations": [],
                    "language": language
                }
            
            # Generate the answer using the RAG chain
            result = self.rag_chain.run(
                context=combined_context,
                question=question,
                language=language
            )
            
            # Process the result to extract citations (in a real implementation, this would be more sophisticated)
            citations = self._extract_citations(context_chunks)
            
            return {
                "answer": result,
                "citations": citations,
                "language": language
            }
        except Exception as e:
            logger.error(f"Error generating answer: {str(e)}")
            raise

    def generate_answer_with_selected_context(self, question: str, selected_context: str, context_chunks: List[Dict[str, Any]], language: str = "en") -> Dict[str, Any]:
        """
        Generate an answer with additional context from user selection.
        
        Args:
            question: The user's question
            selected_context: Additional context provided by the user
            context_chunks: List of context chunks retrieved from the textbook
            language: The language for the response
            
        Returns:
            Dictionary containing the answer and citations
        """
        try:
            # Combine the selected context with retrieved context chunks
            all_context_parts = []
            
            if selected_context:
                all_context_parts.append(f"Selected text: {selected_context}")
            
            context_texts = [chunk['content'] for chunk in context_chunks if chunk.get('content')]
            all_context_parts.extend(context_texts)
            
            combined_context = "\n\n".join(all_context_parts)
            
            if not combined_context.strip():
                # If no context was found, return appropriate response
                return {
                    "answer": "I cannot find an answer to this question in the textbook.",
                    "citations": [],
                    "language": language
                }
            
            # Generate the answer using the RAG chain
            result = self.rag_chain.run(
                context=combined_context,
                question=question,
                language=language
            )
            
            # Process the result to extract citations
            citations = self._extract_citations(context_chunks)
            
            return {
                "answer": result,
                "citations": citations,
                "language": language
            }
        except Exception as e:
            logger.error(f"Error generating answer with selected context: {str(e)}")
            raise

    def _extract_citations(self, context_chunks: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """
        Extract citations from context chunks.
        
        Args:
            context_chunks: List of context chunks with metadata
            
        Returns:
            List of citation dictionaries
        """
        citations = []
        for chunk in context_chunks:
            # In a real implementation, this would link to actual chapter titles
            # For now, we'll use placeholder chapter titles based on the chunk's chapter_id
            citation = {
                "chapter_title": f"Chapter {chunk.get('chapter_id', 'Unknown')}",
                "section_heading": chunk.get('section_heading', 'Unknown Section'),
                "url_anchor": chunk.get('url_anchor', '#')
            }
            citations.append(citation)
        
        return citations

    def validate_answer_relevance(self, question: str, answer: str) -> bool:
        """
        Validate if the generated answer is relevant to the question.
        
        Args:
            question: The original question
            answer: The generated answer
            
        Returns:
            Boolean indicating if the answer is relevant
        """
        # A simple heuristic to check if the answer seems relevant
        # In a real implementation, this would use more sophisticated methods
        if "cannot find an answer" in answer.lower() or "not found in the textbook" in answer.lower():
            return True  # It's a valid response when answer isn't in the book
        
        if len(answer) < 10:  # Answer is too short
            return False
        
        return True