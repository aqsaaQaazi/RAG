# Research for Physical AI & Humanoid Robotics Textbook Feature

## Research Area 1: Primary Backend Language for RAG System

**Task**: Research primary backend language (Python vs. Node.js/TypeScript) suitable for RAG system with lightweight embedding models, CPU-friendly LLMs, Qdrant, and Neon, considering free-tier friendly infrastructure and GitHub Pages deployment.

**Decision**: Python
**Rationale**: Python offers a more mature and extensive ecosystem for LLMs, NLP, and general AI/ML development, with widely adopted libraries like LangChain and Hugging Face Transformers. It also has robust official client libraries for Qdrant and Neon (PostgreSQL).
**Alternatives Considered**: Node.js. While Node.js excels in real-time performance and offers a unified JavaScript stack, its LLM ecosystem is still growing compared to Python's.

## Research Area 2: Testing Frameworks for Frontend and Backend

**Task**: Research appropriate testing frameworks for Docusaurus (frontend) and a RAG backend (Python/Node.js/TypeScript), considering unit, integration, and end-to-end testing.

**Decision**:
*   Frontend (Docusaurus): Jest and React Testing Library.
*   Backend (Python RAG): Pytest for unit testing, and RAGAS/DeepEval/TruLens for RAG-specific evaluation metrics.
**Rationale**: Jest and React Testing Library are standard for React-based applications like Docusaurus, focusing on user-facing functionality. For the RAG backend, Pytest provides a robust framework for unit tests, while specialized RAG evaluation frameworks (RAGAS, DeepEval, TruLens) offer metrics and tools to assess the quality of retrieval and generation, which is crucial for RAG systems.
**Alternatives Considered**: Other JavaScript testing frameworks for frontend (less relevant given Docusaurus's React base), other Python testing frameworks (Pytest is widely adopted and flexible).

## Research Area 3: Deployment Strategy for RAG Backend

**Task**: Research free-tier friendly deployment strategies for a RAG backend (e.g., serverless options like AWS Lambda/Google Cloud Functions, or small PaaS providers) that can integrate with GitHub Pages for the frontend.

**Decision**: Google Cloud Run with Vertex AI (Text Embedding & Gemini 2.5 Flash LLM) and Neon (PostgreSQL) for metadata.
**Rationale**: Google Cloud Run offers a fully managed, scalable serverless platform with a substantial free tier that scales to zero. Vertex AI provides cost-effective embedding models (`text-embedding-004`) and LLMs (Gemini 2.5 Flash with a generous free tier). Neon (PostgreSQL) is already specified for metadata and has good integration with serverless environments. This combination provides a cost-effective and scalable solution for the RAG backend, integrating well with a GitHub Pages frontend.
**Alternatives Considered**:
*   AWS Lambda/API Gateway/Bedrock/S3: Also a strong contender, but Google Cloud's specific free-tier offerings for LLMs and embeddings appear more directly aligned with the "free-tier friendly LLMs" constraint.
*   Vercel: Excellent for frontend hosting and serverless functions, but might require more manual integration with Qdrant/Neon and its LLM integrations are still maturing compared to Python's ecosystem.
