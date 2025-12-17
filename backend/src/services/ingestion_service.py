from typing import List, Dict, Any, Optional
from pydantic import BaseModel
import logging
from pathlib import Path
import markdown
from bs4 import BeautifulSoup
import re

# Import the models and database connection
from src.models.textbook_content import TextbookContent
from src.models.chapter import Chapter
from src.db.database import SessionLocal
from src.utils.qdrant_manager import QdrantManager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChapterMetadata(BaseModel):
    title: str
    order: int
    slug: str
    language: str = "en"


class IngestionService:
    def __init__(self):
        self.qdrant_manager = QdrantManager()
        self.db = SessionLocal()

    def read_markdown_file(self, file_path: str) -> Dict[str, Any]:
        """Read and parse a markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {
                'content': content,
                'filename': Path(file_path).name
            }
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {str(e)}")
            raise

    def extract_chapter_metadata(self, content: str, filename: str) -> ChapterMetadata:
        """Extract chapter metadata from content"""
        # Extract title from the first header
        lines = content.split('\n')
        title = ""
        for line in lines:
            if line.startswith('# '):
                title = line[2:].strip()
                break
            elif line.startswith('title:'):
                title = line[6:].strip()
                break

        # Extract order from filename
        match = re.match(r'(\d+)-', filename)
        order = int(match.group(1)) if match else 0

        # Create slug from title
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower().replace(' ', '-'))
        
        return ChapterMetadata(
            title=title,
            order=order,
            slug=slug
        )

    def extract_key_ideas(self, content: str) -> List[str]:
        """Extract key ideas from the content"""
        key_ideas_section = re.search(r'## Key Ideas\s+(- .+)+', content, re.DOTALL)
        if not key_ideas_section:
            return []

        ideas = []
        for line in key_ideas_section.group(0).split('\n'):
            if line.strip().startswith('- '):
                ideas.append(line.strip()[2:])
        
        return ideas

    def extract_practical_checklist(self, content: str) -> List[str]:
        """Extract practical checklist from the content"""
        checklist_section = re.search(r'## Practical Checklist\s+(- \[.+\] .+)+', content, re.DOTALL)
        if not checklist_section:
            return []

        checklist = []
        for line in checklist_section.group(0).split('\n'):
            if line.strip().startswith('- '):
                checklist.append(line.strip()[2:])
        
        return checklist

    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
        """Split text into overlapping chunks"""
        sentences = re.split(r'[.!?]+', text)
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += " " + sentence
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                
                # Add overlapping text from the end of current chunk to the next
                if len(current_chunk) > overlap:
                    current_chunk = current_chunk[-overlap:] + " " + sentence
                else:
                    current_chunk = sentence
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks

    def process_textbook_content(self, file_path: str) -> Dict[str, Any]:
        """Process a single textbook content file"""
        try:
            # Read the content
            raw_data = self.read_markdown_file(file_path)
            
            # Extract chapter metadata
            metadata = self.extract_chapter_metadata(raw_data['content'], raw_data['filename'])
            
            # Extract key ideas and practical checklist
            key_ideas = self.extract_key_ideas(raw_data['content'])
            practical_checklist = self.extract_practical_checklist(raw_data['content'])
            
            # Extract content without frontmatter and special sections
            content_without_special = re.sub(r'---.*?---', '', raw_data['content'], flags=re.DOTALL)
            
            # Create textbook content record
            textbook_content = TextbookContent(
                filename=raw_data['filename'],
                content=content_without_special,
                language=metadata.language
            )
            
            # Create chapter record
            chapter = Chapter(
                textbook_content_id=textbook_content.id,
                title=metadata.title,
                order=metadata.order,
                slug=metadata.slug,
                content_summary=raw_data['content'][:200] + "...",  # First 200 chars as summary
                key_ideas=str(key_ideas),  # Store as string representation
                practical_checklist=str(practical_checklist)  # Store as string representation
            )
            
            # Chunk the content for RAG
            content_chunks = self.chunk_text(content_without_special)
            
            # Create chunks with metadata for embedding
            chunk_metadata = []
            for i, chunk in enumerate(content_chunks):
                chunk_metadata.append({
                    "chapter_id": str(chapter.id),
                    "section_heading": f"Section {i+1}",
                    "url_anchor": f"#section-{i+1}",
                    "language": metadata.language
                })
            
            return {
                "textbook_content": textbook_content,
                "chapter": chapter,
                "content_chunks": content_chunks,
                "chunk_metadata": chunk_metadata
            }
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {str(e)}")
            raise

    def ingest_textbook(self, directory_path: str) -> bool:
        """Process all markdown files in a directory"""
        try:
            directory = Path(directory_path)
            markdown_files = list(directory.glob("*.md"))
            
            if not markdown_files:
                logger.warning(f"No markdown files found in {directory_path}")
                return False
            
            # Process each markdown file
            all_chunks = []
            all_metadata = []
            
            for file_path in markdown_files:
                logger.info(f"Processing file: {file_path}")
                
                result = self.process_textbook_content(str(file_path))
                
                # Add chunks and metadata to lists for RAG
                all_chunks.extend(result['content_chunks'])
                all_metadata.extend(result['chunk_metadata'])
            
            # Add processed content to Qdrant
            if all_chunks:
                success = self.qdrant_manager.add_texts_with_embeddings(all_chunks, all_metadata)
                if not success:
                    logger.error("Failed to add content to Qdrant")
                    return False
            
            logger.info(f"Successfully ingested {len(markdown_files)} textbook files")
            return True
        except Exception as e:
            logger.error(f"Error during ingestion: {str(e)}")
            return False

    def __del__(self):
        """Clean up resources"""
        if hasattr(self, 'db'):
            self.db.close()