# Project Guidelines for AI-Native Book Platform (CLAUDE.md)

This document outlines the essential guidelines, technology stack, coding conventions, and operational commands for the AI-Native Book Platform, designed for interactive education with AI-driven personalization and translation.

## 1. Project Overview

*   **Name**: "AI-Native Book Platform"
*   **Purpose**: An interactive educational platform with AI-driven personalization and translation.

## 2. Technology Stack

*(Note: Exact versions for frameworks were provided in the prompt as `package.json`, `requirements.txt`, and `pyproject.toml` were not found.)*

*   **Frontend**:
    *   Docusaurus v3
    *   React
    *   TypeScript
    *   Tailwind CSS v3 (Strictly no v4)
    *   Better-Auth Client SDK
*   **Backend**:
    *   FastAPI
    *   Python 3.11+
    *   python-jose (for JWT validation)
    *   Neon Postgres (SQLModel with Multi-tenancy `tenant_id`)
    *   Qdrant Cloud (Vector database)

## 3. Directory Structure

*(Note: `backend/`, `frontend/`, `.claude/skills/`, and `specs/` directories were not found in the codebase at the root level.)*

```
.
├── CLAUDE.md
├── history/
│   ├── adr/
│   ├── audits/
│   └── prompts/
│       └── constitution/
└── .specify/
    ├── memory/
    │   └── constitution.md
    └── templates/
        ├── commands/
        ├── plan-template.md
        ├── phr-template.prompt.md
        ├── spec-template.md
        └── tasks-template.md
```

## 4. Coding Conventions (Critical)

*   **Frontend**:
    *   React Functional Components
    *   Tailwind Utility Classes (No raw CSS)
    *   TypeScript Strict Mode
*   **Backend**:
    *   Python 3.11+
    *   Pydantic Models
    *   Relative Imports in `src/`
*   **Auth**:
    *   Client-Side: `better-auth/react`
    *   Server-Side: `python-jose` for JWT verification

## 5. Key Commands

*   **Backend (Example)**:
    ```bash
    uvicorn main:app --reload
    ```
*   **Frontend (Example)**:
    ```bash
    npm start
    ```
*   **Spec-Kit Plus Commands**:
    *   `/sp.specify`: To create or update feature specifications.
    *   `/sp.implement`: To execute the implementation plan by processing and executing all tasks.

## 6. Important Notes (Bonus Mandates)

*   **Urdu Translation**: Must be a core lesson tab feature, implemented via AI Skill.
*   **Hardware Info**: Must be captured in the User Profile during onboarding.
*   **Reusable Intelligence**: All AI logic must use Skills harvested from `.claude/skills/`.