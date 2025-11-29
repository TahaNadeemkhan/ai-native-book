# Implementation Plan: AI-Native Book Platform

**Branch**: `001-ai-native-book-platform` | **Date**: 2025-11-28 | **Spec**: `specs/001-ai-native-book-platform/spec.md`
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation of an AI-Native Book Platform, an interactive educational platform with AI-driven personalization and translation. It will feature smart authentication and onboarding, a 4-tab lesson interface (Original, Summarize, Personalized, Urdu Translation), and a Hybrid RAG chatbot for Q&A.

## Technical Context

**Language/Version**: Python 3.11+, TypeScript
**Primary Dependencies**: FastAPI, SQLModel, python-jose, Docusaurus v3, React, Tailwind CSS v3, better-auth/react, LangChain, Google Gemini Embeddings, OpenAI Agent SDK, Qdrant Cloud
**Storage**: Neon Postgres, Qdrant Cloud
**Testing**: pytest (backend), React Testing Library (frontend) - Standard Unit Tests (Pytest for Backend logic, Jest for Frontend components).
**Target Platform**: Linux server (backend), Web (frontend)
**Project Type**: web
**Performance Goals**: Lesson pages load all four content tabs within 3 seconds for 90% of users. 90% of chatbot queries receive a relevant and accurate AI-generated response.
**Constraints**: Tailwind CSS v3 (Strictly no v4). All AI logic must be encapsulated in Agent Skills (`.claude/skills/`). Multi-tenancy with `tenant_id` RLS in Neon Postgres.
**Scale/Scope**: Educational platform for students, supporting personalized content and interactive chatbot.


## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Prime Directives Adherence**:
  - [x] `spec.md` is the single source of truth for features.
  - [x] `constitution.md` is the single source of truth for engineering standards.
  - [x] Implementation initiated only after a defined `spec.md` and `plan.md`.
  - [x] Repetitive logic extracted into Agent Skills (`.claude/skills/`).
- [x] **Technology Stack Compliance**:
  - [x] Frontend: Docusaurus v3, React, TypeScript, Tailwind CSS v3 (no v4), `better-auth` Client SDK.
  - [x] Backend: FastAPI, Python 3.11+, `python-jose` for JWT, Neon Postgres (SQLModel) with `tenant_id`, Qdrant Cloud.
- [x] **Functional Requirements Alignment**:
  - [x] Auth & Profile: Hardware Info (GPU/RAM) captured during onboarding.
  - [x] Localization: Urdu Translation via AI Skill as a core lesson tab.
  - [x] Chatbot: RAG implemented with context-aware selection.
- [x] **Engineering Standards Compliance**:
  - [x] Code Quality: Strict TypeScript (frontend), Pydantic models (backend).
  - [x] History & Governance: Strict folder hierarchy (`history/prompts/`, `history/adr/`, `history/audits/`). PHR created after every significant task. ADRs for architectural decisions.
- [x] **Failure Prevention Measures**:
  - [x] Dependency Lock: No major version upgrades (e.g., Tailwind v4) without an ADR.
  - [x] Secrets: No hardcoded API keys; `.env` usage enforced.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Structure Decision**: The project will use a web application structure with separate `backend/` and `frontend/` directories, aligning with the specified Docusaurus and FastAPI technology stack. The `backend/` will contain `src/` for models, services, and API endpoints, along with `tests/`. Similarly, `frontend/` will have `src/` for components, pages, and services, and its own `tests/` directory.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
