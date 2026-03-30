# Implementation Tasks: AI-Native Book Platform

**Feature Branch**: `001-ai-native-book-platform`
**Created**: 2025-11-29
**Status**: Draft
**Input**: Generated from `plan.md`, `spec.md`, `data-model.md`, and `research.md`

This document outlines the detailed, actionable tasks for implementing the AI-Native Book Platform, organized by user story for independent development and testing.

## Phase 1: Setup

These tasks focus on initializing the project structure and foundational configurations based on the `plan.md` and `CLAUDE.md`.

- [ ] T001 Create `backend/` directory with `src/`, `models/`, `services/`, `api/`, and `tests/` subdirectories.
- [ ] T002 Create `frontend/` directory with `src/`, `components/`, `pages/`, `services/`, and `tests/` subdirectories.
- [ ] T003 Configure base FastAPI application in `backend/src/main.py`.
- [ ] T004 Configure Docusaurus v3 in `frontend/` for basic site structure.
- [ ] T005 Integrate Tailwind CSS v3 into the frontend project.

## Phase 2: Foundational Tasks

These tasks establish core prerequisites that all user stories depend on, including database setup and shared utilities.

- [ ] T006 Set up `SQLModel` for database interactions in `backend/src/database.py`.
- [ ] T007 Implement multi-tenancy with `tenant_id` for Neon Postgres, ensuring Row Level Security (RLS) as described in `data-model.md`.
- [ ] T008 Configure `python-jose` for JWT validation in backend authentication.
- [ ] T009 Set up environment variable loading (e.g., using `python-dotenv` for backend, Docusaurus env setup for frontend).

## Phase 3: User Story 1 - Smart Auth & Onboarding (Priority: High)

**Story Goal**: As a new user, I want to sign up via GitHub so I can access personalized content.
**Independent Test**: User can successfully sign up via GitHub and complete the onboarding modal, with profile data (including hardware info) persisted in the database.

- [ ] T010 [P] [US1] Create `User` model in `backend/src/models/user.py` with `id`, `tenant_id`, `email`, and `additional_info` (JSONB) fields.
- [ ] T011 [P] [US1] Implement GitHub OAuth integration using `better-auth/react` in `frontend/src/services/auth.ts`.
- [ ] T012 [P] [US1] Create GitHub OAuth callback endpoint in `backend/src/api/auth.py` for token exchange and user creation/login.
- [ ] T013 [P] [US1] Develop onboarding modal component in `frontend/src/components/OnboardingModal.tsx` to capture programming proficiency, AI proficiency, and hardware background.
- [ ] T014 [US1] Create API endpoint in `backend/src/api/user.py` to update user's `additional_info` with onboarding data.
- [ ] T015 [US1] Implement logic in `frontend/src/pages/index.tsx` (or similar entry point) to display onboarding modal on first login.
- [ ] T016 [US1] Add unit tests for `User` model in `backend/tests/test_user_model.py`.
- [ ] T017 [US1] Add integration tests for GitHub OAuth flow and onboarding data persistence in `backend/tests/test_auth_onboarding.py`.

## Phase 4: User Story 2 - The 4-Tab Lesson Interface (Priority: High)

**Story Goal**: As a student, I want to view lessons in different formats to suit my learning style.
**Independent Test**: A lesson page displays 4 tabs (Original, Summarize, Personalized, Urdu Translation), each showing the correct content.

- [ ] T018 [P] [US2] Create `Lesson` model in `backend/src/models/lesson.py` with `id`, `tenant_id`, `content`, `summary`, `is_summary_generated` fields.
- [ ] T019 [P] [US2] Create `PersonalizedContent` model in `backend/src/models/personalized_content.py` with `id`, `user_id`, `lesson_id`, `content` fields.
- [ ] T020 [P] [US2] Develop API endpoint in `backend/src/api/lesson.py` to retrieve original lesson content.
- [ ] T021 [P] [US2] Develop API endpoint in `backend/src/api/lesson.py` to trigger and retrieve AI-generated summaries (using `lesson-summarizer` skill).
- [ ] T022 [P] [US2] Develop API endpoint in `backend/src/api/lesson.py` to trigger and retrieve AI-personalized content (using `content-personalizer` skill).
- [ ] T023 [P] [US2] Develop API endpoint in `backend/src/api/lesson.py` to trigger and retrieve AI-generated Urdu translations (using `urdu-translator` skill).
- [ ] T024 [US2] Create a generic `TabbedLessonViewer` component in `frontend/src/components/TabbedLessonViewer.tsx` to display the four tabs (Original, Summarize, Personalized, Urdu Translation).
- [ ] T025 [US2] Implement logic in `frontend/src/pages/LessonPage.tsx` to fetch content for each tab from the backend and display it using the `TabbedLessonViewer`.
- [ ] T026 [US2] Add unit tests for `Lesson` and `PersonalizedContent` models in `backend/tests/test_lesson_models.py`.
- [ ] T027 [US2] Add integration tests for the 4-tab lesson interface, ensuring correct content display and AI skill invocation in `frontend/tests/test_lesson_tabs.test.tsx`.

## Phase 5: User Story 3 - Hybrid RAG Chatbot (Priority: Medium)

**Story Goal**: As a student, I want to ask questions about the book and get accurate answers.
**Independent Test**: A floating chatbot widget allows users to ask questions and receive context-aware answers from the AI.

- [ ] T028 [P] [US3] Implement content ingestion script for Google Gemini Embeddings to vectorize book content and store in Qdrant Cloud. (This might be a separate utility script, e.g., `backend/scripts/ingest.py`).
- [ ] T029 [P] [US3] Develop API endpoint in `backend/src/api/chatbot.py` to receive user queries.
- [ ] T030 [P] [US3] Implement retrieval logic using Google Gemini Embeddings and Qdrant Cloud in `backend/src/services/rag_service.py`.
- [ ] T031 [P] [US3] Integrate OpenAI Agent SDK in `backend/src/services/rag_service.py` to generate responses based on retrieved context.
- [ ] T032 [US3] Create a floating chatbot widget component in `frontend/src/components/ChatbotWidget.tsx`.
- [ ] T033 [US3] Implement client-side logic in `frontend/src/components/ChatbotWidget.tsx` to send user queries to the backend chatbot API.
- [ ] T034 [US3] Implement context-menu option in `frontend/src/services/context_menu.ts` (or similar) to "Ask AI" for selected text, integrating with the chatbot widget.
- [ ] T035 [US3] Add unit tests for RAG service logic (embedding, retrieval, response generation) in `backend/tests/test_rag_service.py`.
- [ ] T036 [US3] Add integration tests for the chatbot widget, including context-menu interaction and AI response display in `frontend/tests/test_chatbot.test.tsx`.

## Phase 6: Polish & Cross-Cutting Concerns

These tasks address overall system quality, performance, and final touches.

- [ ] T037 Implement error handling and fallback mechanisms for AI skill failures (e.g., display original content or a friendly message).
- [ ] T038 Optimize lesson content loading and AI processing for large lessons to meet performance goals (3 seconds for 90% of users).
- [ ] T039 Review and refine UI/UX for all new components (onboarding modal, tabbed lesson viewer, chatbot widget).
- [ ] T040 Ensure all AI logic uses Skills harvested from `.claude/skills/` as per project guidelines.
- [ ] T041 Implement comprehensive logging for backend services.
- [ ] T042 Conduct end-to-end testing of the entire platform to ensure all features work together seamlessly.

## Dependencies

User Story 1 -> User Story 2 -> User Story 3

- **Phase 1: Setup** must be completed before any other phase.
- **Phase 2: Foundational Tasks** must be completed before any User Story phase.
- **User Story 1: Smart Auth & Onboarding** is a prerequisite for a fully functional platform, enabling personalized content.
- **User Story 2: The 4-Tab Lesson Interface** depends on User Story 1 for personalized content access.
- **User Story 3: Hybrid RAG Chatbot** can be developed in parallel with User Story 2, but its full context-aware functionality benefits from lesson content being available.

## Parallel Execution Examples

### User Story 1
- `T010 [P] [US1] Create User model in backend/src/models/user.py`
- `T011 [P] [US1] Implement GitHub OAuth integration using better-auth/react in frontend/src/services/auth.ts`
- `T012 [P] [US1] Create GitHub OAuth callback endpoint in backend/src/api/auth.py`
- `T013 [P] [US1] Develop onboarding modal component in frontend/src/components/OnboardingModal.tsx`

### User Story 2
- `T018 [P] [US2] Create Lesson model in backend/src/models/lesson.py`
- `T019 [P] [US2] Create PersonalizedContent model in backend/src/models/personalized_content.py`
- `T020 [P] [US2] Develop API endpoint in backend/src/api/lesson.py to retrieve original lesson content`
- `T021 [P] [US2] Develop API endpoint in backend/src/api/lesson.py to trigger and retrieve AI-generated summaries`
- `T022 [P] [US2] Develop API endpoint in backend/src/api/lesson.py to trigger and retrieve AI-personalized content`
- `T023 [P] [US2] Develop API endpoint in backend/src/api/lesson.py to trigger and retrieve AI-generated Urdu translations`

### User Story 3
- `T028 [P] [US3] Implement content ingestion script for Google Gemini Embeddings to vectorize book content and store in Qdrant Cloud.`
- `T029 [P] [US3] Develop API endpoint in backend/src/api/chatbot.py to receive user queries.`
- `T030 [P] [US3] Implement retrieval logic using Google Gemini Embeddings and Qdrant Cloud in backend/src/services/rag_service.py.`
- `T031 [P] [US3] Integrate OpenAI Agent SDK in backend/src/services/rag_service.py to generate responses based on retrieved context.`

## Implementation Strategy

The implementation will follow an MVP-first approach, iteratively delivering features in priority order.

1.  **MVP Scope**: User Story 1 (Smart Auth & Onboarding) and a basic implementation of User Story 2 (Original and Summarize tabs only) will form the initial MVP to establish core user flow and content delivery.
2.  **Incremental Delivery**: User Story 3 (Hybrid RAG Chatbot), and the remaining tabs of User Story 2 (Personalized, Urdu Translation) will be developed and integrated incrementally.
3.  **Test-Driven where applicable**: Unit tests will be written alongside code development for critical backend logic and frontend components. Integration and end-to-end tests will validate cross-component functionality.
4.  **Agent Skill Integration**: AI-driven features will prioritize the creation and integration of Agent Skills as per project guidelines.
