<!--
Sync Impact Report:
Version change: 0.0.0 -> 1.0.0
Modified principles: None (initial creation)
Added sections: Prime Directives, Technology Mandates, Functional Requirements, Engineering Standards, Failure Prevention
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/*.md: ⚠ pending
- README.md: ⚠ pending
- docs/quickstart.md: ⚠ pending
Follow-up TODOs: None
-->
# ai-native-book Constitution

## Core Principles

### 1. Prime Directives (The "Why" & "How")
*   **Single Source of Truth**: The `spec.md` is the absolute authority for features. The `constitution.md` is the absolute authority for engineering standards.
*   **Spec-Driven Development (SDD)**: No implementation begins without a defined Spec and Plan.
*   **Agentic Workflow**: All repetitive logic must be harvested into **Agent Skills** (`.claude/skills/`).

### 2. Technology Mandates (The Stack)
*   **Frontend**: Docusaurus v3 + React + TypeScript.
    *   **Styling**: Tailwind CSS **v3** ONLY (Do not use v4).
    *   **Auth**: `better-auth` Client SDK.
*   **Backend**: FastAPI + Python 3.11+.
    *   **Verification**: `python-jose` for JWT validation.
    *   **Database**: Neon Postgres (SQLModel) with Multi-tenancy (`tenant_id`).
    *   **Vector**: Qdrant Cloud.

### 3. Functional Requirements (Bonus Constraints)
*   **Auth & Profile**: Must capture **Hardware Info** (GPU/RAM) during onboarding.
*   **Localization**: Must include **Urdu Translation** (via AI Skill) as a core lesson tab.
*   **Chatbot**: Must implement RAG with context-aware selection.

### 4. Engineering Standards
*   **Code Quality**: Strict TypeScript for frontend. Pydantic models for backend.
*   **History & Governance**:
    *   Maintain strict folder hierarchy: `history/prompts/`, `history/adr/`, `history/audits/`.
    *   Create a **PHR** after every significant task.
    *   Document architectural decisions in **ADRs**.

### 5. Failure Prevention
*   **Dependency Lock**: Do not upgrade major versions (e.g., Tailwind v4) without an ADR.
*   **Secrets**: Never hardcode API keys; use `.env`.

## Governance
This constitution supersedes all other project practices and documentation. Amendments to this document require:
1.  A formal proposal outlining the change and its rationale.
2.  Review and approval by the Principal Software Architect.
3.  Documentation in an Architectural Decision Record (ADR) if the amendment introduces a significant architectural decision.
4.  A migration plan for existing systems if the amendment is backward incompatible.
All code reviews and project activities must verify compliance with the principles outlined herein.

**Version**: 1.0.0 | **Ratified**: 2025-11-28 | **Last Amended**: 2025-11-28
