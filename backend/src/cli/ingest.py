import argparse
import sys
import os
from pathlib import Path

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.services.ingestion_service import IngestionService


def main():
    parser = argparse.ArgumentParser(description='Ingest textbook content for RAG system')
    parser.add_argument(
        'input_directory',
        type=str,
        help='Directory containing markdown files to ingest'
    )
    parser.add_argument(
        '--chunk-size',
        type=int,
        default=1000,
        help='Size of text chunks for embedding (default: 1000)'
    )
    parser.add_argument(
        '--overlap',
        type=int,
        default=100,
        help='Overlap between chunks (default: 100)'
    )
    parser.add_argument(
        '--language',
        type=str,
        default='en',
        help='Language of the content (default: en)'
    )

    args = parser.parse_args()

    # Validate input directory
    input_path = Path(args.input_directory)
    if not input_path.exists():
        print(f"Error: Input directory {args.input_directory} does not exist")
        sys.exit(1)
    
    if not input_path.is_dir():
        print(f"Error: {args.input_directory} is not a directory")
        sys.exit(1)

    # Initialize ingestion service
    ingestion_service = IngestionService()

    # Perform ingestion
    print(f"Starting ingestion from {args.input_directory}")
    success = ingestion_service.ingest_textbook(args.input_directory)
    
    if success:
        print("Ingestion completed successfully!")
        sys.exit(0)
    else:
        print("Ingestion failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()