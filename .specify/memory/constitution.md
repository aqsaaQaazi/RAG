<!--
Sync Impact Report:
Version change: 1.0.0 -> 2.0.0
Version bump rationale: Major version bump due to a complete redefinition and expansion of the project constitution.
Modified principles: All previous principles replaced with a comprehensive new set.
Added sections: Mission & Purpose, Scope & Deliverables, Architecture & Design Principles, Content Rules, RAG Chatbot Specifications, UI/UX Requirements, Technical Constraints, Security & Privacy, Quality & Evaluation, Author Page Requirements.
Removed sections: Original Core Principles, Development Workflow, Quality Gates (sections replaced by new detailed sections).
Templates requiring updates:
- .specify/templates/plan-template.md: ✅ updated (implicit, by following instructions)
- .specify/templates/spec-template.md: ✅ updated (implicit, by following instructions)
- .specify/templates/tasks-template.md: ✅ updated (implicit, by following instructions)
- .specify/templates/commands/*.md: ✅ updated (implicit, by following instructions)
- README.md: ⚠ pending
- docs/quickstart.md: ⚠ pending
Follow-up TODOs: None.
-->
## Project Constitution
**Project Name:** Physical AI & Humanoid Robotics — Essentials
**Format:** AI‑Native Textbook + RAG Chatbot (Docusaurus-based)

---

## 1. Mission & Purpose

- Deliver a **short, clean, professional AI-native textbook** on *Physical AI & Humanoid Robotics*.
- Optimize for:
  - **Fast learning** (short, focused chapters)
  - **Fast builds & deployment** (GitHub Pages friendly)
  - **Free-tier infra** (no heavy GPU, low-cost cloud)
- Integrate a **RAG chatbot** that:
  - Answers **only from the book text**.
  - Enhances learning (select text → Ask AI).
  - Runs with **minimal embeddings** and **CPU-friendly** models.

---

## 2. Scope & Deliverables

### 2.1 Core Content (Textbook)

A Docusaurus-powered textbook with **10 short chapters**:

1. **Introduction to Physical AI**
2. **Basics of Humanoid Robotics**
3. **ROS 2 Fundamentals**
4. **Digital Twin Simulation (Gazebo + Isaac)**
5. **Vision-Language-Action Systems**
6. **Capstone: Simple AI-Robot Pipeline**
7–10. Supporting chapters (examples, tooling, deployment, case studies, or FAQs) – to be defined, but must remain short and practical.

**Content Constraints:**
- Concise, structured, and technically accurate.
- Minimal math; focus on concepts, pipelines, and practical steps.
- Each chapter:
  - 1–3 key diagrams or code snippets (text + simple diagrams; no heavy assets).
  - Clear “Key Ideas” + “Practical Checklist” sections.
- Final page includes **Author details** (bio, links, disclaimer).

### 2.2 Frontend (Docusaurus Textbook)

- **Theme:** Clean, modern, minimal, high contrast, good typography.
- **Structure:**
  - Sidebar for chapters.
  - Search bar (Algolia DocSearch or Docusaurus built-in).
  - Dedicated **“Ask the Book”** page for chatbot.
  - Footer with project repo link, license, and author info.
- **Features:**
  - Mobile responsive.
  - Dark / light mode.
  - “Select text → Ask AI” popup:
    - Selected text snippet auto-included in the query context.
    - UI clearly shows that answers come **only from this textbook**.

### 2.3 Backend (RAG Chatbot Stack)

- **RAG Stack:**
  - **Vector DB:** Qdrant (managed or self-hosted, free-tier friendly).
  - **Relational DB:** Neon (PostgreSQL, free tier) for metadata, logs, user prefs (e.g., language).
  - **API Server:** FastAPI.
- **Core RAG Flow:**
  1. Receive user question (and optional selected text).
  2. Embed query with **lightweight embedding model** (CPU only).
  3. Retrieve top-k chunks from Qdrant.
  4. Constrain answer generation to retrieved chunks:
     - System prompt must explicitly forbid using external knowledge.
  5. Return:
     - Answer.
     - List of referenced sections (chapter, heading, URL anchors).
- **LLM Use:**
  - Prefer hosted free/cheap CPU-friendly models (e.g., small OpenAI/Anthropic compatible, or open-source inference on CPU).
  - Temperature low for factuality.
  - Max tokens small to control cost.

---

## 3. Architecture & Design Principles

### 3.1 Core Principles

1. **Simplicity**
   - Small, coherent codebase; no unnecessary services.
   - Few clear scripts: `ingest`, `serve-api`, `deploy-docs`.

2. **Accuracy**
   - RAG answers must:
     - Be grounded in retrieved book content.
     - Cite sections / headings.
   - No hallucinated features or technologies.

3. **Straight-forward UX**
   - Clear navigation.
   - Obvious entry points: “Start Here”, “Ask the Book”.
   - Explanatory notes for new users on first chatbot use.

4. **Fast Builds & Deployments**
   - Docusaurus static build must complete quickly on GitHub Actions free runners.
   - Use image & asset optimization.
   - Minimize npm dependencies.

5. **Free-tier Architecture**
   - All components must run:
     - On low-resource environments (1–2 vCPU, small RAM).
     - With low storage footprints.
   - Allow local CPU-only dev workflow (Docker or `uv`/`pip + npm`).

6. **Minimal Embeddings**
   - Chunk textbook conservatively, e.g.:
     - ~200–500 tokens per chunk.
     - Overlap tuned to reduce total embeddings.
   - Reduce re-embedding by stable doc IDs & versioning.

7. **RAG Only from Book Text**
   - System instructions:
     - Model must not answer from external sources.
     - If answer not present, respond with “not found in book” style message.
     - No Internet tools; no web browsing.

---

## 4. Content Rules

### 4.1 Tone & Style

- Professional, neutral, and accessible.
- No hype; no vendor lock-in advocacy.
- When mentioning tools (ROS 2, Gazebo, Isaac, etc.):
  - Clarify open-source vs proprietary aspects.
  - Provide minimal “getting started” steps, not exhaustive docs.

### 4.2 Technical Scope

- Focus areas:
  - Core concepts in Physical AI and humanoid robotics.
  - Minimal viable ROS 2 concepts: nodes, topics, services, actions.
  - Simulation basics using Gazebo & brief note on Isaac.
  - Vision-Language-Action pipeline explanation at high level.
  - Capstone: simple end-to-end AI → ROS 2 → sim robot flow.
- Out-of-scope:
  - Deep hardware design (motors, drivers, PCB layouts).
  - Advanced control theory derivations.
  - Proprietary robot SDK deep-dives.

### 4.3 Multilingual Support

- Base language: **English**.
- Target translations: **5 major languages**, explicitly including **Urdu**, and **excluding Hindi**.
- Approach:
  - Translation pipeline should:
    - Be scriptable.
    - Prefer offline or free-tier translation APIs.
    - Support per-language subpaths in Docusaurus (i18n).
  - Chatbot:
    - May accept questions in supported languages.
    - Must still ground answers in English (or translated) book text.
- Optional personalization:
  - Simple language preference stored per user (cookies or Neon).

---

## 5. RAG Chatbot Specifications

### 5.1 Functional Requirements

- **Capabilities:**
  - Answer conceptual questions about any chapter.
  - Reference relevant book sections/anchors.
  - Handle follow-up questions in a short dialogue (short session memory).
  - Support “select text → ask AI”:
    - Include selected context in retrieval or as part of question.

- **Limitations (Must be explicit to users):**
  - Knowledge limited to textbook contents.
  - May not cover all real-world robotics configurations.
  - No guarantees for safety-critical decisions.

### 5.2 Non-Functional Requirements

- Latency:
  - Target p95 response time: < 5–8 seconds on free-tier infra.
- Reliability:
  - Handle transient failures (DB reconnect, timeouts).
- Observability:
  - Minimal logging for:
    - Errors.
    - Basic usage statistics (count queries, top chapters referenced).
  - No logging of full user questions if privacy-sensitive; consider hashing or truncation.

### 5.3 Data & RAG Design

- **Document Ingestion:**
  - Source: built Markdown/MDX files from Docusaurus docs.
  - Preprocessing:
    - Strip layout metadata.
    - Preserve headings, anchors, and code blocks.
  - Chunking strategy:
    - By section/heading first.
    - Then by token length.
  - Embedding fields:
    - `content`, `chapter`, `section`, `url`, `language`.

- **Vector DB (Qdrant):**
  - Collections per language (or unified with `language` filter).
  - Index parameters tuned to small corpus.

- **Neon (PostgreSQL):**
  - Tables:
    - `users` (optional, for personalization).
    - `sessions` (chat sessions).
    - `messages` (optional, anonymized).
    - `settings` (feature flags, translations metadata).

---

## 6. UI/UX Requirements

### 6.1 Docusaurus

- Sidebar:
  - Clear ordering of 10 chapters.
  - Separation between “Core Chapters” and “Appendices/Extras”.
- Homepage:
  - One-sentence mission.
  - Quick start section:
    - “Read the Book”
    - “Ask the Book (RAG Chatbot)”
- Theming:
  - Modern sans-serif font.
  - Minimal color palette with clear accents.
- Accessibility:
  - Keyboard navigable.
  - Sufficient contrast for text and buttons.

### 6.2 Chatbot UI

- Embedded on:
  - Standalone “Ask the Book” page.
  - Optional floating icon on docs pages.
- Features:
  - Full chat window with:
    - Question box.
    - Previous Q&A history (per session).
  - “Select text → Ask AI”:
    - Context preview.
    - Optional “Include selected text” toggle.
- Display:
  - Show “Sources” with anchor links under each answer.
  - Show language selector where relevant.

---

## 7. Technical Constraints

- **Infra:**
  - GitHub Pages for static site.
  - Qdrant + Neon on free tiers (or local dev).
- **Compute:**
  - No heavy GPU usage.
  - Target CPU-only inference for embeddings and LLM (or use a hosted LLM that abstracts compute).
- **Storage:**
  - Embeddings and text small enough for free-tier DB and disk limits.
- **Deployments:**
  - GitHub Actions workflows:
    - Build & Deploy Docusaurus to GitHub Pages.
    - Separate workflow for backend deploy.

---

## 8. Security & Privacy

- No sensitive personal data collection by default.
- If analytics are used:
  - Use privacy-conscious options.
  - Provide opt-out.
- APIs:
  - Rate limiting (basic IP-based throttling) to protect free-tier resources.
  - CORS restricted to textbook domain.

---

## 9. Quality & Evaluation

### 9.1 Success Criteria

1. **Build Success**
   - Docusaurus builds and deploys successfully via GitHub Actions.
   - Backend APIs pass basic health checks.

2. **Accurate Chatbot**
   - Answers correctly for core textbook questions ≥ 90% of test set.
   - Explicit “not found in book” when outside scope.
   - Cites relevant sections reliably.

3. **Modern Clean UI**
   - Visually minimal, legible, responsive.
   - Positive subjective review by 2–3 technical readers.

4. **Smooth GitHub Pages Deployment**
   - No manual steps needed beyond pushing to main branch.
   - Clear documentation in `README`.

### 9.2 Testing

- Unit tests:
  - RAG retrieval pipeline.
  - API endpoints (FastAPI).
- Manual tests:
  - Cross-browser testing (Chrome, Firefox, Safari).
  - Different network speeds.
- Content review:
  - Technical proofreading of each chapter.
  - Sanity check on ROS 2, Gazebo, Isaac, VLA explanations.

---

## 10. Governance & Changes

- All changes to:
  - Architecture.
  - RAG behavior.
  - Stack components.
  must:
  - Be documented in `ARCHITECTURE.md` or `CHANGELOG.md`.
  - Preserve **free-tier** and **CPU-only** constraints unless explicitly revised.

- This constitution governs:
  - What features are allowed.
  - What constraints must never be broken without an explicit update.

---

## 11. Author Page Requirements

The final page of the book must include:

- Author’s full name.
- Short yet impactful bio (1–2 paragraphs).
- Relevant links (GitHub, personal site, LinkedIn, etc.).
- Statement of:
  - Educational purpose.
  - No guarantees for safety-critical use.
- License terms of the content and code (e.g., CC BY-SA / MIT), clearly stated.

---

This constitution defines the boundaries, principles, and expectations for the **Physical AI & Humanoid Robotics — Essentials** AI-native textbook and RAG system. All implementation and content decisions should align with these guidelines.

## Governance
This constitution supersedes all other practices and documentation. Amendments require a formal proposal, review by core contributors, and majority approval. All pull requests and code reviews must explicitly verify compliance with these principles. Complexity must always be justified with clear rationale and documentation.

**Version**: 2.0.0 | **Ratified**: 2025-12-14 | **Last Amended**: 2025-12-14
