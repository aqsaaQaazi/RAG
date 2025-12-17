# RAG Textbook Constitution

## Core Principles

### I. Library-First
Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries

### II. CLI Interface
Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced

### IV. Integration Testing
Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas

### V. Observability
Text I/O ensures debuggability; Structured logging required; Error handling must provide clear operational insights while protecting user privacy

### VI. Simplicity
Start simple, YAGNI principles; Add complexity only when justified by measurable benefits; Prefer simple solutions that meet requirements

## Additional Constraints

Technology stack requirements:
- Use free-tier friendly infrastructure (Google Cloud Run, Vertex AI, Neon, Qdrant)
- Maintain support for 5 major languages (including Urdu, excluding Hindi)
- Implement RAG system with lightweight embedding models and CPU-friendly LLMs
- Optimize for fast builds and deployment to GitHub Pages

## Development Workflow

- All features must start with a clear specification
- Implementation must follow the architectural plan
- Testing framework established (Pytest for backend, Jest/RTL for frontend, RAGAS for RAG-specific evaluation)
- Integration tests needed for RAG pipeline (ingestion→embedding→retrieval→generation)

## Governance

Constitution supersedes all other practices; Amendments require documentation, approval, migration plan

All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance

**Version**: 1.0.0 | **Ratified**: 2025-12-17 | **Last Amended**: 2025-12-17
