# Research: Simple Static Documentation Website (No RAG)

## Decision: Remove RAG functionality and backend components
- **Rationale**: To simplify the website as requested, all RAG (Retrieval Augmented Generation) functionality and backend services will be removed.
- **Implementation**: Remove all backend-related files and code, including Python files, FastAPI, LangChain components, and any backend directory.

## Decision: Simplify header to only contain navigation and book name
- **Rationale**: The header needs to include only essential navigation elements and the book name, without logos or other extra elements as specified.
- **Implementation**: Update Docusaurus configuration to customize the navbar with only necessary elements (book name, 'Start Reading', 'View on GitHub' and theme switcher).

## Decision: Maintain theme switching functionality
- **Rationale**: Theme switching remains important for user experience and accessibility.
- **Implementation**: Preserve the theme switching functionality with automatic detection of system preference and manual override option.

## Decision: Use static site generation
- **Rationale**: Static site generation provides faster loading times and better SEO, removing the need for any backend services.
- **Implementation**: Rely on Docusaurus static site generation capabilities with no dynamic API calls.

## Decision: Remove unused API contracts
- **Rationale**: Since the RAG backend is being removed, the API contracts related to it are no longer necessary.
- **Implementation**: Remove any backend API contract files since the website will be static.

## Decision: Maintain accessibility features
- **Rationale**: Accessibility remains critical as per the constitution principles.
- **Implementation**: Keep semantic HTML elements and other accessibility features while removing RAG functionality.

## Alternatives considered:
- For RAG functionality: Keep vs. remove - chose removal to meet simplification requirement
- For architecture: Dynamic API vs. static site - chose static site to meet simplification requirement
- For dependencies: Keep all vs. minimal set - chose minimal set to reduce complexity