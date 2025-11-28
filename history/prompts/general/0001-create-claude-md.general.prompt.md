---
id: 0001
title: Create CLAUDE.md
stage: general
date: 2025-11-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: TODO(USER): user name not available
command: Help me create a comprehensive `CLAUDE.md` file for this project.



**Task: Analyze the codebase and generate `CLAUDE.md`**



Please include these 6 specific sections based on what you see in the files AND the rules I provide below:



1.  **Project Overview:**

    * Name: "AI-Native Book Platform"

    * Purpose: An interactive educational platform with AI-driven personalization and translation.



2.  **Technology Stack:**

    * Scan `package.json`, `requirements.txt`, and `pyproject.toml` to list the exact versions of frameworks (Docusaurus, FastAPI, Tailwind v3, Better-Auth, Neon, Qdrant).



3.  **Directory Structure:**

    * Generate a tree structure of the key folders: `backend/`, `frontend/`, `history/`, `.claude/skills/`, `specs/`.



4.  **Coding Conventions (Critical):**

    * **Frontend:** React Functional Components, Tailwind Utility Classes (No raw CSS), TypeScript Strict Mode.

    * **Backend:** Python 3.11+, Pydantic Models, Relative Imports in `src/`.

    * **Auth:** Use `better-auth/react` for Client-Side, `python-jose` for Server-Side verification.



5.  **Key Commands:**

    * List commands to run Backend (`uvicorn...`) and Frontend (`npm start...`).

    * List commands for Spec-Kit Plus (`/sp.specify`, `/sp.implement`).



6.  **Important Notes (Bonus Mandates):**

    * **Urdu Translation:** Must be a core feature.

    * **Hardware Info:** Must be captured in User Profile.

    * **Reusable Intelligence:** All AI logic must use Skills from `.claude/skills/`.



**Action:** Generate this file and save it to the root as `CLAUDE.md`.
labels: ["documentation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - CLAUDE.md
tests:
null
---

## Prompt

Help me create a comprehensive `CLAUDE.md` file for this project.



**Task: Analyze the codebase and generate `CLAUDE.md`**



Please include these 6 specific sections based on what you see in the files AND the rules I provide below:



1.  **Project Overview:**

    * Name: "AI-Native Book Platform"

    * Purpose: An interactive educational platform with AI-driven personalization and translation.



2.  **Technology Stack:**

    * Scan `package.json`, `requirements.txt`, and `pyproject.toml` to list the exact versions of frameworks (Docusaurus, FastAPI, Tailwind v3, Better-Auth, Neon, Qdrant).



3.  **Directory Structure:**

    * Generate a tree structure of the key folders: `backend/`, `frontend/`, `history/`, `.claude/skills/`, `specs/`.



4.  **Coding Conventions (Critical):**

    * **Frontend:** React Functional Components, Tailwind Utility Classes (No raw CSS), TypeScript Strict Mode.

    * **Backend:** Python 3.11+, Pydantic Models, Relative Imports in `src/`.

    * **Auth:** Use `better-auth/react` for Client-Side, `python-jose` for Server-Side verification.



5.  **Key Commands:**

    * List commands to run Backend (`uvicorn...`) and Frontend (`npm start...`).

    * List commands for Spec-Kit Plus (`/sp.specify`, `/sp.implement`).



6.  **Important Notes (Bonus Mandates):**

    * **Urdu Translation:** Must be a core feature.

    * **Hardware Info:** Must be captured in User Profile.

    * **Reusable Intelligence:** All AI logic must use Skills from `.claude/skills/`.



**Action:** Generate this file and save it to the root as `CLAUDE.md`.

## Response snapshot

I have created the `CLAUDE.md` file based on your requirements. It includes sections for Project Overview, Technology Stack, Directory Structure, Coding Conventions, Key Commands, and Important Notes. I noted that some directory structures and package files were not found, so the technology stack versions were taken directly from your prompt, and the directory structure reflects what was present.

## Outcome

- ✅ Impact: Successfully generated the `CLAUDE.md` file with specified sections and content, including details from the provided project context and my findings.
- 🧪 Tests: N/A
- 📁 Files: Created `CLAUDE.md`.
- 🔁 Next prompts: N/A
- 🧠 Reflection: The task was completed by meticulously extracting information from the user prompt and inferring from the codebase where possible. Noted the absence of `package.json`, `requirements.txt`, `pyproject.toml`, `backend/`, `frontend/`, and `.claude/skills/` which impacted the technology stack versioning and directory structure generation, but I proceeded with the information provided in the prompt.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
