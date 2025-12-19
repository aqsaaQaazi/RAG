---
id: "007"
title: "English-Only Website Planning"
stage: "plan"
date: "2025-12-19"
surface: "agent"
model: "Qwen"
feature: "master"
branch: "master"
user: "user"
command: "/sp.plan i need no other languages except english, remve all that stuff. plus header must not have any logos or stuff except navigations and book name."
labels: ["docusaurus", "english-only", "ui", "frontend"]
links:
  spec: "specs/master/spec.md"
  plan: "specs/master/plan.md"
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - "specs/master/plan.md"
  - "specs/master/spec.md"
  - "specs/master/research.md"
  - "specs/master/data-model.md"
  - "specs/master/contracts/api-contracts.yaml"
  - "specs/master/quickstart.md"
  - ".specify/memory/constitution.md"
tests: []
outcome: "Successfully updated specification for English-only content and simplified header"
evaluation: "Removed multilingual support, updated header requirements, maintained core functionality"
---

# English-Only Website Planning

## User Input
```
/sp.plan i need no other languages except english, remve all that stuff. plus header must not have any logos or stuff except navigations and book name.
```

## Summary

Successfully updated the implementation plan to reflect the new requirements:

1. Removed multilingual support (Urdu, etc.) and retained only English content
2. Updated the header requirements to only include navigation and book name
3. Preserved core functionality (theme switching, accessibility features)
4. Updated all documentation artifacts to reflect these changes

## Changes Made

1. **spec.md**: Updated user stories and functional requirements to specify English-only content and simplified header
2. **plan.md**: Updated implementation plan to reflect English-only nature and simplified header requirements
3. **constitution.md**: Modified internationalization principle to account for English-only release while maintaining future extensibility
4. **research.md**: Created research document outlining decisions for simplification
5. **data-model.md**: Updated data model to reflect English-only content structure
6. **api-contracts.yaml**: Updated API contracts to reflect English-only endpoints
7. **quickstart.md**: Created quickstart guide with English-only instructions and simplified header configuration

## Verification

- All references to Urdu and multilingual functionality have been removed
- Header requirements now specify only navigation elements and book name (no logos)
- Core functionality like theme switching is preserved
- Accessibility requirements remain intact
- Architecture maintains readiness for future multilingual support