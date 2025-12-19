# Implementation Plan: Simple Static Documentation Website (No RAG)

**Branch**: `master` | **Date**: 2025-12-19 | **Spec**: [link to spec]
**Input**: Feature specification from `/specs/master/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature implements a simple Docusaurus-based static documentation website without any RAG (Retrieval Augmented Generation) functionality. The implementation focuses on serving static content with a clean homepage at the root URL, simplified header with only navigation and book name, and full English-only documentation content. The site includes theme switching (light/dark) and accessibility features, but removes all backend API functionality and dynamic content generation.

## Technical Context

**Language/Version**: JavaScript/TypeScript (for Docusaurus), Node.js v18+ for build process
**Primary Dependencies**: Docusaurus v3.x, React 18+, @docusaurus/preset-classic
**Storage**: Static file hosting (GitHub Pages) - no database or backend API
**Testing**: Jest for unit tests, Cypress for end-to-end tests, React Testing Library for component tests
**Target Platform**: Static website optimized for modern browsers (Chrome, Firefox, Safari, Edge)
**Project Type**: Static site with no backend services
**Performance Goals**: Fast builds and deployment to GitHub Pages, page load time <3 seconds on average connection
**Constraints**: Static content only (no dynamic API calls), WCAG 2.1 AA compliance for accessibility, SEO-optimized with semantic HTML, no external dependencies for core functionality
**Scale/Scope**: Single documentation site with English-only content

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Gate 1: Accessibility First
- **Status**: PASSED
- **Justification**: The design will use semantic HTML elements, follow WCAG 2.1 AA standards, and be tested with screen readers to ensure accessibility.

### Gate 2: User Experience Priority
- **Status**: PASSED
- **Justification**: The design prioritizes a clean, simple homepage at the root URL with intuitive navigation elements (Start Reading, GitHub link, theme switcher).

### Gate 3: Test-First (NON-NEGOTIABLE)
- **Status**: PASSED
- **Justification**: Testing framework established (Jest, Cypress, React Testing Library) with plans to write tests for all functionality before implementation.

### Gate 4: Performance Conscious
- **Status**: PASSED
- **Justification**: Using static site generation with Docusaurus ensures fast loading times, and performance metrics will be monitored to ensure <3s load times and 90+ Lighthouse scores.

### Gate 5: Simplicity and Clarity
- **Status**: PASSED
- **Justification**: Starting with core functionality (simple homepage, theme switching, English-only documentation) following YAGNI principles. Content will be written in simple, easy-to-understand language.

### Gate 6: Internationalization Support
- **Status**: PASSED
- **Justification**: While implementing English-only content for this release, the architecture will maintain readiness for future multilingual support by preserving i18n-ready structures.

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
```

### Source Code (repository root)

frontend/
├── docs/                  # English documentation content only
│   ├── 01-introduction.md
│   ├── 02-foundations-of-physical-ai.md
│   ├── 03-humanoid-robot-design.md
│   ├── 04-locomotion-and-control.md
│   ├── 05-sensing-and-perception.md
│   ├── 06-learning-algorithms.md
│   ├── 07-hardware-integration.md
│   ├── 08-ethics-and-safety.md
│   ├── 09-future-directions.md
│   └── 10-conclusion.md
├── src/
│   ├── components/        # Custom reusable React components (no RAG components)
│   │   ├── HomepageFeatures.js      # Homepage features section
│   │   └── ThemeToggle.js          # Theme switching component
│   ├── pages/             # React components for non-docs pages
│   │   └── index.js       # Custom homepage component (no RAG chat interface)
│   └── css/               # Custom styles
├── static/                # Static files (images, icons, etc.)
├── package.json           # NPM package configuration
├── docusaurus.config.js   # Main Docusaurus configuration (English-only)
├── sidebars.js            # Sidebar navigation configuration (minimal)
└── babel.config.js        # Babel configuration

specs/master/contracts/
└── static-content-api.yaml     # (No RAG API contracts - this would be removed)

**Structure Decision**: Selected the static website structure with Docusaurus for documentation only. The project will have a custom homepage at the root URL, with documentation content in English only. All RAG (Retrieval Augmented Generation) functionality removed.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |