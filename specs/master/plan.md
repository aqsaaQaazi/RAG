# Implementation Plan: Physical AI & Humanoid Robotics Textbook

**Branch**: `master` | **Date**: 2025-12-17 | **Spec**: [link to spec]
**Input**: Feature specification from `/specs/1-generate-textbook/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature implements a Physical AI & Humanoid Robotics textbook with an integrated RAG chatbot. The system consists of a Docusaurus-powered frontend for textbook presentation and a Python-based RAG backend that provides contextual answers from the textbook content using vector embeddings in Qdrant and metadata in Neon PostgreSQL.

The solution uses Google Cloud Run for backend deployment, Vertex AI for embeddings and LLMs, and GitHub Pages for frontend hosting. The approach emphasizes free-tier friendly infrastructure while maintaining the ability to answer user questions with proper citations to specific textbook sections.

## Technical Context

**Language/Version**: Python 3.8+ (for RAG backend), JavaScript/TypeScript (for Docusaurus frontend)
**Primary Dependencies**:
  - Backend: FastAPI, LangChain, Hugging Face Transformers, Qdrant client, Neon (PostgreSQL) client, Google Cloud Vertex AI SDK
  - Frontend: Docusaurus, React
**Storage**: Qdrant (vector database for embeddings), Neon (PostgreSQL) for metadata storage
**Testing**: Pytest (backend unit tests), RAGAS/DeepEval/TruLens (RAG-specific evaluation), Jest and React Testing Library (frontend)
**Target Platform**: Web application (Docusaurus frontend served via GitHub Pages, Python RAG backend deployed on Google Cloud Run)
**Project Type**: Web application with backend API (Docusaurus frontend + Python RAG backend API)
**Performance Goals**:
  - RAG chatbot response time (p95) under 8 seconds on free-tier infrastructure
  - Fast builds and deployment to GitHub Pages
  - Efficient ingestion and embedding of textbook content
**Constraints**:
  - Free-tier friendly infrastructure (Google Cloud Run, Vertex AI, Neon, Qdrant)
  - Lightweight embedding models and CPU-friendly LLMs (or hosted equivalents)
  - Low temperature and small max tokens settings for LLMs
  - Minimal logging (avoid privacy-sensitive user questions)
  - RAG answers grounded only in textbook content
**Scale/Scope**:
  - 10 short chapters of Physical AI & Humanoid Robotics textbook
  - Support for 5 major languages (including Urdu, excluding Hindi)
  - Support for citation of sources with chapter, heading, and URL anchors

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Gate 1: Library-First Approach
- **Status**: PASSED
- **Justification**: The RAG system will be built as a modular library with clear separation of concerns (data processing, embedding, retrieval, generation) that can potentially be reused.

### Gate 2: CLI Interface
- **Status**: PASSED
- **Justification**: The backend will expose functionality via a CLI for data ingestion, and the API will follow text-in/text-out protocols.

### Gate 3: Test-First (NON-NEGOTIABLE)
- **Status**: PASSED
- **Justification**: Testing framework established (Pytest for backend, Jest/RTL for frontend, RAGAS for RAG-specific evaluation).

### Gate 4: Integration Testing
- **Status**: PASSED
- **Justification**: Integration tests needed for RAG pipeline (ingestion→embedding→retrieval→generation) and inter-service communication (frontend→backend→Qdrant/Neon).

### Gate 5: Observability and Performance
- **Status**: PASSED
- **Justification**: Logging requirements defined (minimal for privacy) with performance goal of <8s response time (p95) on free-tier infrastructure.

### Gate 6: Simplicity
- **Status**: PASSED
- **Justification**: Starting with core functionality first (10-chapter textbook with RAG chatbot) following YAGNI principles.

## Project Structure

### Documentation (this feature)

```text
specs/master/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)

specs/1-generate-textbook/
└── spec.md              # Feature specification
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── textbook_content.py      # Textbook content entity
│   │   ├── chapter.py               # Chapter entity
│   │   ├── text_chunk.py            # Text chunk entity
│   │   ├── user_query.py            # User query entity
│   │   ├── chatbot_answer.py        # Chatbot answer entity
│   │   └── source_citation.py       # Source citation entity
│   ├── services/
│   │   ├── rag_service.py           # Main RAG service
│   │   ├── embedding_service.py     # Embedding generation and storage
│   │   ├── retrieval_service.py     # Text retrieval from vector database
│   │   ├── generation_service.py    # Answer generation with citations
│   │   └── ingestion_service.py     # Content ingestion and preprocessing
│   ├── api/
│   │   ├── main.py                  # FastAPI app definition
│   │   ├── routes/
│   │   │   ├── chat.py              # Chatbot API endpoints
│   │   │   └── ingestion.py         # Ingestion API endpoints
│   │   └── middleware/
│   │       └── cors.py              # CORS configuration
│   └── cli/
│       └── ingest.py                # CLI for content ingestion
├── tests/
│   ├── unit/
│   │   ├── models/
│   │   ├── services/
│   │   └── api/
│   ├── integration/
│   │   └── rag_pipeline_test.py     # Full RAG pipeline integration tests
│   └── contract/
│       └── rag_api_test.py          # API contract tests
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Containerization for deployment
└── config/
    └── settings.py                  # Configuration settings

frontend/
├── docs/
│   ├── 01-introduction.md           # Chapter 1
│   ├── 02-foundations-of-physical-ai.md  # Chapter 2
│   ├── 03-humanoid-robot-design.md  # Chapter 3
│   ├── 04-locomotion-and-control.md # Chapter 4
│   ├── 05-sensing-and-perception.md # Chapter 5
│   ├── 06-learning-algorithms.md    # Chapter 6
│   ├── 07-hardware-integration.md   # Chapter 7
│   ├── 08-ethics-and-safety.md      # Chapter 8
│   ├── 09-future-directions.md      # Chapter 9
│   └── 10-conclusion.md             # Chapter 10
├── src/
│   ├── components/
│   │   ├── TextbookViewer.jsx       # Textbook reader component
│   │   ├── ChatWithBook.jsx         # RAG chat interface
│   │   ├── SelectionPopup.jsx       # Text selection popup
│   │   └── LanguageSelector.jsx     # Language selection component
│   ├── pages/
│   │   ├── AskTheBook.jsx           # Dedicated "Ask the Book" page
│   │   └── AuthorDetails.jsx        # Author details page
│   └── css/
│       └── custom.css               # Custom styling
├── static/
│   ├── img/
│   │   └── humanoid-robot.svg       # Robotic diagrams and images
│   └── js/
│       └── text-selection.js        # Text selection feature implementation
├── docusaurus.config.js             # Docusaurus configuration
├── sidebars.js                      # Sidebar navigation configuration
├── package.json                     # Frontend dependencies
└── i18n/                            # Internationalization files
    ├── en/
    ├── ur/
    └── es/                          # And 3 other language directories
```

**Structure Decision**: Selected the web application structure option with separate backend and frontend directories. The backend uses a Python-based RAG architecture with FastAPI, while the frontend uses Docusaurus with React for the textbook presentation and chatbot interface.

## Summary of Planning

This implementation plan details the architecture for a Physical AI & Humanoid Robotics textbook with an integrated RAG chatbot. The plan includes:

- Technical context with specific technologies, dependencies, and constraints
- Constitution check ensuring the approach aligns with project principles
- Detailed project structure for both backend and frontend components
- All necessary components for the RAG system, multilingual support, and textbook presentation

The plan is now complete and ready for the next phase: detailed task breakdown and implementation.

