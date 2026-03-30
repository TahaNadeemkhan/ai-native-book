---
id: 0001
title: Initial Project Constitution
stage: constitution
date: 2025-11-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: TODO(USER): user name not available
command: /sp.constitution Act as a Principal Software Architect. Write a high-performance Project Constitution for "ai-native-book". This document defines the non-negotiable laws of the project.



### 1. Prime Directives (The "Why" & "How")

* **Single Source of Truth:** The `spec.md` is the absolute authority for features. The `constitution.md` is the absolute authority for engineering standards.

* **Spec-Driven Development (SDD):** No implementation begins without a defined Spec and Plan.

* **Agentic Workflow:** All repetitive logic must be harvested into **Agent Skills** (`.claude/skills/`).



### 2. Technology Mandates (The Stack)

* **Frontend:** Docusaurus v3 + React + TypeScript.

    * **Styling:** Tailwind CSS **v3** ONLY (Do not use v4).

    * **Auth:** `better-auth` Client SDK.

* **Backend:** FastAPI + Python 3.11+.

    * **Verification:** `python-jose` for JWT validation.

    * **Database:** Neon Postgres (SQLModel) with Multi-tenancy (`tenant_id`).

    * **Vector:** Qdrant Cloud.



### 3. Functional Requirements (Bonus Constraints)

* **Auth & Profile:** Must capture **Hardware Info** (GPU/RAM) during onboarding.

* **Localization:** Must include **Urdu Translation** (via AI Skill) as a core lesson tab.

* **Chatbot:** Must implement RAG with context-aware selection.



### 4. Engineering Standards

* **Code Quality:** Strict TypeScript for frontend. Pydantic models for backend.

* **History & Governance:**

    * Maintain strict folder hierarchy: `history/prompts/`, `history/adr/`, `history/audits/`.

    * Create a **PHR** after every significant task.

    * Document architectural decisions in **ADRs**.



### 5. Failure Prevention:

* **Dependency Lock:** Do not upgrade major versions (e.g., Tailwind v4) without an ADR.

* **Secrets:** Never hardcode API keys; use `.env`.
labels: ["architecture","constitution"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
null
---

## Prompt

Act as a Principal Software Architect. Write a high-performance Project Constitution for "ai-native-book". This document defines the non-negotiable laws of the project.



### 1. Prime Directives (The "Why" & "How")

* **Single Source of Truth:** The `spec.md` is the absolute authority for features. The `constitution.md` is the absolute authority for engineering standards.

* **Spec-Driven Development (SDD):** No implementation begins without a defined Spec and Plan.

* **Agentic Workflow:** All repetitive logic must be harvested into **Agent Skills** (`.claude/skills/`).



### 2. Technology Mandates (The Stack)

* **Frontend:** Docusaurus v3 + React + TypeScript.

    * **Styling:** Tailwind CSS **v3** ONLY (Do not use v4).

    * **Auth:** `better-auth` Client SDK.

* **Backend:** FastAPI + Python 3.11+.

    * **Verification:** `python-jose` for JWT validation.

    * **Database:** Neon Postgres (SQLModel) with Multi-tenancy (`tenant_id`).

    * **Vector:** Qdrant Cloud.



### 3. Functional Requirements (Bonus Constraints)

* **Auth & Profile:** Must capture **Hardware Info** (GPU/RAM) during onboarding.

* **Localization:** Must include **Urdu Translation** (via AI Skill) as a core lesson tab.

* **Chatbot:** Must implement RAG with context-aware selection.



### 4. Engineering Standards

* **Code Quality:** Strict TypeScript for frontend. Pydantic models for backend.

* **History & Governance:**

    * Maintain strict folder hierarchy: `history/prompts/`, `history/adr/`, `history/audits/`.

    * Create a **PHR** after every significant task.

    * Document architectural decisions in **ADRs**.



### 5. Failure Prevention

* **Dependency Lock:** Do not upgrade major versions (e.g., Tailwind v4) without an ADR.

* **Secrets:** Never hardcode API keys; use `.env`.

## Response snapshot

The Project Constitution for "ai-native-book" has been successfully created and saved to `.specify/memory/constitution.md`.

**New Version:** 1.0.0 (Major version bump due to initial creation of the foundational project document).

**Files flagged for manual follow-up:**
- `.specify/templates/commands/*.md`: Pending (Directory not found, unable to verify consistency)
- `README.md`: Pending (File not found, unable to verify consistency)
- `docs/quickstart.md`: Pending (File not found, unable to verify consistency)

**Suggested commit message:**
`docs: Initial project constitution for "ai-native-book" v1.0.0`

## Outcome

- ✅ Impact: Successfully created the project constitution and updated related templates.
- 🧪 Tests: N/A
- 📁 Files: Created .specify/memory/constitution.md, updated .specify/templates/plan-template.md and .specify/templates/spec-template.md.
- 🔁 Next prompts: Review pending template updates.
- 🧠 Reflection: Successfully generated and applied the constitution. Encountered missing command directory and readme file, which need follow-up.
## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
