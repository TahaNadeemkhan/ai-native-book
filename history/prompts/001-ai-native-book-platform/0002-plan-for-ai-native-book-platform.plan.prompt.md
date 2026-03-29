---
id: 0002
title: Plan for AI-Native Book Platform
stage: plan
date: 2025-11-29
surface: CLI
model: claude-sonnet-4-5-20250929
feature: 001-ai-native-book-platform
branch: 001-ai-native-book-platform
user: user
command: /sp.plan
labels: [plan-generation]
links:
  spec: /mnt/d/piaic/cli-practice/ai-native-book/specs/001-ai-native-book-platform/spec.md
  ticket:
  adr:
  pr:
files:
  - /mnt/d/piaic/cli-practice/ai-native-book/CLAUDE.md (read)
  - /mnt/d/piaic/cli-practice/ai-native-book/specs/001-ai-native-book-platform/spec.md (read)
  - /mnt/d/piaic/cli-practice/ai-native-book/specs/001-ai-native-book-platform/plan.md (written)
  - /mnt/d/piaic/cli-practice/ai-native-book/history/prompts/001-ai-native-book-platform/0002-plan-for-ai-native-book-platform.plan.prompt.md (written)
tests:
  - No direct tests were run.
---

## Prompt

Create the Technical Implementation Plan for "AI-Native Book Platform".

Ensure strict adherence to the Constitution and avoid previous failure modes.

### 1. System Architecture
*   **Frontend:** Docusaurus v3 (TypeScript) + **Tailwind CSS v3** (Strictly v3).
    *   **Auth:** Use `better-auth/react` Client SDK.
    *   **State:** React Context for User Profile (Hardware Info, Proficiency).
*   **Backend:** FastAPI (Python 3.11).
    *   **Auth:** Verify JWT using `python-jose` (No `better-auth` pip package).
    *   **DB:** Neon Serverless (SQLModel with `tenant_id` RLS).
    *   **AI:** Hybrid RAG (LangChain/Google for Embeddings + OpenAI Agents SDK for Reasoning).
*   **Intelligence:** Logic stored in `.claude/skills/` (Personalizer, Translator, Summarizer).

### 2. Database Schema (Neon)
*   `users`: `id`, `tenant_id`, `email`, `additional_info` (JSONB: {hardware, programming_level, ai_level}).
*   `lessons`: `id`, `tenant_id`, `content`, `summary` (Text), `is_summary_generated` (Bool).
*   `personalized_content`: `id`, `user_id`, `lesson_id`, `content`.
*   `vectors`: Qdrant collection `book_knowledge` (Managed via API).

### 3. Implementation Phases

#### **Phase 1: Foundation & Backend**
*   Setup `backend/` with FastAPI + SQLModel.
*   Create `init_db.py` to initialize Neon tables.
*   Implement `auth.py` using `python-jose` to verify Bearer tokens.
*   Create Core APIs: `GET /lessons`, `POST /personalize`, `POST /translate` (using Skills).

#### **Phase 2: Intelligence & Hybrid RAG**
*   Create Agent Skills in `.claude/skills/`.
*   **Ingestion Script:** Create `ingest_book.py` to read docs, embed via **Google Gemini**, and store in Qdrant.
*   **Chat API:** Implement `POST /chat/query` (Retrieve via Google -> Reason via OpenAI).

#### **Phase 3: Frontend & Bonus UI**
*   Initialize Docusaurus + **Tailwind v3**.
*   Implement `AuthToggle` (Sign In/Out).
*   **Onboarding Modal:** Capture **Hardware Info** (Mandatory Bonus).
*   **Lesson Layout:** Swizzle `DocItem` to add **4 Tabs** (Original, Summary, Personalized, **Urdu**).

#### **Phase 4: Final Integration**
*   Connect Chat Widget to Backend.
*   End-to-End Testing of all Bonus Features.

**Output:** Generate `specs/001-ai-native-book-platform/plan.md`.

## Response snapshot

This plan outlines the implementation of an AI-Native Book Platform, an interactive educational platform with AI-driven personalization and translation. It will feature smart authentication and onboarding, a 4-tab lesson interface (Original, Summarize, Personalized, Urdu Translation), and a Hybrid RAG chatbot for Q&A. The plan details the technical stack, project structure, and implementation phases (Foundation & Backend, Intelligence & Hybrid RAG, Frontend & Bonus UI, Final Integration), ensuring adherence to constitutional guidelines.

## Outcome

- ✅ Impact: Generated `plan.md` for the AI-Native Book Platform feature.
- 🧪 Tests: No direct tests were run.
- 📁 Files: Created `plan.md`. Read `CLAUDE.md`, `spec.md`.
- 🔁 Next prompts: User will likely proceed with task generation (`/sp.tasks`).
- 🧠 Reflection: Successfully generated the implementation plan, adhering to constitutional guidelines and technical constraints.

## Evaluation notes (flywheel)

- Failure modes observed:
- Graders run and results (PASS/FAIL):
- Prompt variant (if applicable):
- Next experiment (smallest change to try):
