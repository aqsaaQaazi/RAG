# Feature Specification: Generate Physical AI & Humanoid Robotics Textbook

**Feature Branch**: `1-generate-textbook`
**Created**: 2025-12-15
**Status**: Draft
**Input**: User description: "generate textbook."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Read Textbook Chapters (Priority: P1)

As a learner, I want to easily navigate and read the 10 short chapters of the Physical AI & Humanoid Robotics textbook to gain fundamental knowledge.

**Why this priority**: This is the core purpose of the textbook, providing essential learning content.

**Independent Test**: Can be fully tested by accessing the deployed Docusaurus site and navigating through all chapters. Delivers core educational value.

**Acceptance Scenarios**:

1. **Given** I access the textbook website, **When** I navigate the sidebar, **Then** I can see and select all 10 chapters in logical order.
2. **Given** I select a chapter, **When** the chapter content loads, **Then** I see concise, structured, and technically accurate text with minimal math, including 1-3 key diagrams or code snippets.
3. **Given** I am reading a chapter, **When** I scroll to the end, **Then** I can see “Key Ideas” and “Practical Checklist” sections.

---

### User Story 2 - Ask the Book (RAG Chatbot Interaction) (Priority: P1)

As a learner, I want to use the integrated RAG chatbot to ask questions specifically about the textbook content and receive grounded answers with cited sources.

**Why this priority**: This enhances learning by providing interactive, context-aware assistance, a key differentiator from the constitution.

**Independent Test**: Can be fully tested by asking questions through the “Ask the Book” page and verifying answers are accurate and cited from the textbook. Delivers interactive learning value.

**Acceptance Scenarios**:

1. **Given** I am on the “Ask the Book” page, **When** I enter a question related to the textbook content, **Then** the chatbot provides an accurate answer grounded *only* in the book text.
2. **Given** the chatbot provides an answer, **When** I review the response, **Then** it includes a list of referenced sections with anchor links (chapter, heading, URL anchors).
3. **Given** I select a text snippet from a chapter, **When** I use the “Select text → Ask AI” popup feature, **Then** the selected text is included as context for my query and the chatbot answers from the book text.

---

### User Story 3 - Multilingual Content Access (Priority: P2)

As a global learner, I want to access the textbook and interact with the chatbot in multiple supported languages to broaden accessibility.

**Why this priority**: Broadens the reach of the textbook as specified in the constitution (4.3 Multilingual Support).

**Independent Test**: Can be tested by switching the website language and verifying content and chatbot responses are presented in the selected language, grounded in the (translated) book text.

**Acceptance Scenarios**:

1. **Given** I am on the textbook website, **When** I select one of the 5 major supported languages (including Urdu), **Then** the textbook content is displayed in that language.
2. **Given** the textbook is displayed in a non-English language, **When** I ask a question to the chatbot in that language, **Then** the chatbot provides an answer in the same language, grounded in the book text.

---

### Edge Cases

- What happens when a user asks a question not covered by the textbook content? The chatbot must explicitly state that the answer is "not found in the book" or a similar message, as per Constitution 3.1 Core Principles (7. RAG Only from Book Text) and 5.1 Functional Requirements (Limitations).
- How does the system handle very long user questions or selected text snippets? The system should gracefully truncate or summarize the input to fit the lightweight embedding model and LLM constraints, without losing the core intent.
- What happens if the RAG retrieval fails or returns irrelevant chunks? The chatbot should indicate that it cannot provide a grounded answer and follow the "not found in book" behavior.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST generate a Docusaurus-powered static textbook site with 10 short chapters on Physical AI & Humanoid Robotics. (Constitution 2.1, 2.2)
- **FR-002**: The textbook chapters MUST be concise, structured, technically accurate, and include 1-3 diagrams/code snippets, "Key Ideas", and "Practical Checklist" sections. (Constitution 2.1)
- **FR-003**: The textbook website MUST include a clear sidebar navigation, search bar, and a dedicated "Ask the Book" page for the chatbot. (Constitution 2.2, 6.1)
- **FR-004**: The system MUST integrate a RAG chatbot capable of answering questions *only* from the textbook content. (Constitution 1, 2.3, 3.1 (7), 5.1)
- **FR-005**: The RAG chatbot MUST provide answers with cited references (chapter, heading, URL anchors) from the textbook. (Constitution 2.3, 5.1)
- **FR-006**: The chatbot UI MUST support a "select text → Ask AI" feature, incorporating the selected text as query context. (Constitution 2.2, 5.1, 6.2)
- **FR-007**: The system MUST implement multilingual support for the textbook content and chatbot in 5 major languages, including Urdu and excluding Hindi. (Constitution 4.3)
- **FR-008**: The RAG system MUST use Qdrant as the vector database and Neon (PostgreSQL) for metadata, running on free-tier friendly infrastructure. (Constitution 2.3, 7)
- **FR-009**: The RAG system MUST utilize lightweight embedding models and CPU-friendly LLMs (or hosted equivalent) with low temperature and small max tokens. (Constitution 2.3, 7)
- **FR-010**: The system MUST generate an author details page with a bio, relevant links, educational purpose statement, safety disclaimer, and content/code license terms. (Constitution 2.1, 11)
- **FR-011**: The system MUST optimize for fast builds and deployment to GitHub Pages. (Constitution 1, 3.1 (4), 7)
- **FR-012**: The system MUST ensure minimal logging for errors and basic usage statistics in the chatbot backend, avoiding privacy-sensitive user questions. (Constitution 5.2, 8)

### Key Entities *(include if feature involves data)*

- **Textbook Content**: The raw Markdown/MDX files for chapters, diagrams, and code snippets.
- **Chapter**: A discrete section of the textbook with a title, content, key ideas, and practical checklist.
- **Text Chunk**: Segmented pieces of textbook content used for RAG ingestion and retrieval, linked to its original chapter, section, and URL.
- **User Query**: Text input from the user for the RAG chatbot.
- **Chatbot Answer**: The response generated by the LLM, grounded in retrieved textbook content.
- **Source Citation**: References to specific parts of the textbook (chapter, heading, URL) supporting a chatbot answer.
- **Language Preference**: User's chosen language for the textbook and chatbot.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The Docusaurus site MUST successfully build and deploy to GitHub Pages via GitHub Actions with 100% success rate.
- **SC-002**: The RAG chatbot MUST answer correctly for core textbook questions ≥ 90% of a defined test set.
- **SC-003**: The chatbot MUST explicitly respond with a "not found in book" message when questions are outside the textbook's scope in ≥ 95% of relevant test cases.
- **SC-004**: The chatbot MUST cite relevant sections reliably (≥ 95% accuracy) for all grounded answers.
- **SC-005**: The textbook UI MUST be visually minimal, legible, and responsive across common desktop and mobile browsers.
- **SC-006**: The chatbot response time (p95) MUST be under 8 seconds on free-tier infrastructure.
- **SC-007**: The complete textbook (including translations) MUST build and deploy within GitHub Actions free runner time limits.
- **SC-008**: The ingestion process MUST successfully chunk and embed all textbook content into Qdrant.
