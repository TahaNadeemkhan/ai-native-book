---
id: 0001
title: AI-Native Book Platform Specification
stage: spec
date: 2025-11-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-ai-native-book-platform
branch: 001-ai-native-book-platform
user: TODO(USER): user name not available
command: Act as a Senior Product Manager. Create a comprehensive Feature Specification for the "AI-Native Book Platform".

### 1. Product Intent
Build an interactive, multi-tenant educational platform where students learn via AI-adapted content. The system uses a Hybrid RAG architecture (Google Gemini for Embeddings, OpenAI Agent SDK for Reasoning).

### 2. User Stories & Success Criteria (SMART)

#### A. Smart Auth & Onboarding (Priority: High)
* Story: As a new user, I want to sign up via GitHub so I can access personalized content.
* Requirement: Upon first login, the system MUST show a modal to capture:
    1.  **Programming Proficiency:** (Beginner/Intermediate/Expert).
    2.  **AI Proficiency:** (Beginner/Intermediate/Expert).
    3.  **Hardware Background:** (e.g., "RTX 3060, 16GB RAM") -> *Mandatory Bonus Requirement*.
* Success: User profile is created in Neon DB with all 3 fields stored in `additional_info` JSONB column.

#### B. The 4-Tab Lesson Interface (Priority: High)
* Story: As a student, I want to view lessons in different formats to suit my learning style.
* Requirement: Every lesson page must have 4 Tabs:
    1.  **Original:** The static Markdown content.
    2.  **Summarize:** AI-generated bullet points (using `lesson-summarizer` skill).
    3.  **Personalized:** Content rewritten for my proficiency level (using `content-personalizer` skill).
    4.  **Urdu Translation:** Full lesson translated to Urdu (using `urdu-translator` skill) -> *Mandatory Bonus Requirement*.

#### C. Hybrid RAG Chatbot (Priority: Medium)
* Story: As a student, I want to ask questions about the book and get accurate answers.
* Architecture:
    * Ingestion: Script uses **Google Gemini Embeddings** to vectorize book content -> Qdrant.
    * Retrieval: User query vector (Google Gemini) -> Search Qdrant.
    * Answer: **OpenAI Agent** generates response using retrieved context.
* UI: Floating widget support context-menu (select text -> "Ask AI").

### 3. Technical Constraints
* Frontend: Docusaurus v3 + Tailwind CSS v3 (Strict).
* Backend: FastAPI + Neon Postgres (RLS enabled).
* Agentic Workflow: All AI logic MUST be encapsulated in **Agent Skills** (`.claude/skills/`).

### 4. Non-Goals
* No payment processing.
* No video hosting.

**Output:** Create the file `specs/001-ai-native-book-platform/spec.md`.
labels: ["product", "specification", "feature"]
links:
  spec: specs/001-ai-native-book-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-ai-native-book-platform/spec.md
 - specs/001-ai-native-book-platform/checklists/requirements.md
tests:
null
---

## Prompt

Act as a Senior Product Manager. Create a comprehensive Feature Specification for the "AI-Native Book Platform".

### 1. Product Intent
Build an interactive, multi-tenant educational platform where students learn via AI-adapted content. The system uses a Hybrid RAG architecture (Google Gemini for Embeddings, OpenAI Agent SDK for Reasoning).

### 2. User Stories & Success Criteria (SMART)

#### A. Smart Auth & Onboarding (Priority: High)
* Story: As a new user, I want to sign up via GitHub so I can access personalized content.
* Requirement: Upon first login, the system MUST show a modal to capture:
    1.  **Programming Proficiency:** (Beginner/Intermediate/Expert).
    2.  **AI Proficiency:** (Beginner/Intermediate/Expert).
    3.  **Hardware Background:** (e.g., "RTX 3060, 16GB RAM") -> *Mandatory Bonus Requirement*.
* Success: User profile is created in Neon DB with all 3 fields stored in `additional_info` JSONB column.

#### B. The 4-Tab Lesson Interface (Priority: High)
* Story: As a student, I want to view lessons in different formats to suit my learning style.
* Requirement: Every lesson page must have 4 Tabs:
    1.  **Original:** The static Markdown content.
    2.  **Summarize:** AI-generated bullet points (using `lesson-summarizer` skill).
    3.  **Personalized:** Content rewritten for my proficiency level (using `content-personalizer` skill).
    4.  **Urdu Translation:** Full lesson translated to Urdu (using `urdu-translator` skill) -> *Mandatory Bonus Requirement*.

#### C. Hybrid RAG Chatbot (Priority: Medium)
* Story: As a student, I want to ask questions about the book and get accurate answers.
* Architecture:
    * Ingestion: Script uses **Google Gemini Embeddings** to vectorize book content -> Qdrant.
    * Retrieval: User query vector (Google Gemini) -> Search Qdrant.
    * Answer: **OpenAI Agent** generates response using retrieved context.
* UI: Floating widget support context-menu (select text -> "Ask AI").

### 3. Technical Constraints
* Frontend: Docusaurus v3 + Tailwind CSS v3 (Strict).
* Backend: FastAPI + Neon Postgres (RLS enabled).
* Agentic Workflow: All AI logic MUST be encapsulated in **Agent Skills** (`.claude/skills/`).

### 4. Non-Goals
* No payment processing.
* No video hosting.

**Output:** Create the file `specs/001-ai-native-book-platform/spec.md`.

## Response snapshot

The feature specification for the "AI-Native Book Platform" has been successfully created and validated.

**Feature Branch:** `001-ai-native-book-platform`
**Specification File:** `specs/001-ai-native-book-platform/spec.md`
**Quality Checklist:** `specs/001-ai-native-book-platform/checklists/requirements.md`

All specification quality checks passed. The feature is now ready for the planning phase (`/sp.plan`).

## Outcome

- ✅ Impact: Successfully created and validated the feature specification, ready for planning.
- 🧪 Tests: N/A
- 📁 Files: Created `specs/001-ai-native-book-platform/spec.md` and `specs/001-ai-native-book-platform/checklists/requirements.md`.
- 🔁 Next prompts: Proceed to the planning phase using `/sp.plan`.
- 🧠 Reflection: Successfully generated and validated the feature specification based on user input. Handled directory creation and checklist generation as part of the process.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
