# Feature Specification: AI-Native Book Platform

**Feature Branch**: `001-ai-native-book-platform`
**Created**: 2025-11-28
**Status**: Draft
**Input**: User description: "Act as a Senior Product Manager. Create a comprehensive Feature Specification for the \"AI-Native Book Platform\".\n\n\n\n### **1. Product Intent**\n\nBuild an interactive, multi-tenant educational platform where students learn via AI-adapted content. The system uses a Hybrid RAG architecture (Google Gemini for Embeddings, OpenAI Agent SDK for Reasoning).\n\n\n\n### **2. User Stories & Success Criteria (SMART)**\n\n\n\n#### **A. Smart Auth & Onboarding (Priority: High)**\n\n* **Story:** As a new user, I want to sign up via GitHub so I can access personalized content.\n\n* **Requirement:** Upon first login, the system MUST show a modal to capture:\n\n    1.  **Programming Proficiency:** (Beginner/Intermediate/Expert).\n\n    2.  **AI Proficiency:** (Beginner/Intermediate/Expert).\n\n    3.  **Hardware Background:** (e.g., \"RTX 3060, 16GB RAM\") -> *Mandatory Bonus Requirement*.\n\n* **Success:** User profile is created in Neon DB with all 3 fields stored in `additional_info` JSONB column.\n\n\n\n#### **B. The 4-Tab Lesson Interface (Priority: High)**\n\n* **Story:** As a student, I want to view lessons in different formats to suit my learning style.\n\n* **Requirement:** Every lesson page must have 4 Tabs:\n\n    1.  **Original:** The static Markdown content.\n\n    2.  **Summarize:** AI-generated bullet points (using `lesson-summarizer` skill).\n\n    3.  **Personalized:** Content rewritten for my proficiency level (using `content-personalizer` skill).\n\n    4.  **Urdu Translation:** Full lesson translated to Urdu (using `urdu-translator` skill) -> *Mandatory Bonus Requirement*.\n\n\n\n#### **C. Hybrid RAG Chatbot (Priority: Medium)**\n\n* **Story:** As a student, I want to ask questions about the book and get accurate answers.\n\n* **Architecture:**\n\n    * **Ingestion:** Script uses **Google Gemini Embeddings** to vectorize book content -> Qdrant.\n\n    * **Retrieval:** User query vector (Google Gemini) -> Search Qdrant.\n\n    * **Answer:** **OpenAI Agent** generates response using retrieved context.\n\n* **UI:** Floating widget support context-menu (select text -> \"Ask AI\").\n\n\n\n### **3. Technical Constraints**\n\n* **Frontend:** Docusaurus v3 + Tailwind CSS v3 (Strict).\n\n* **Backend:** FastAPI + Neon Postgres (RLS enabled).\n\n* **Agentic Workflow:** All AI logic MUST be encapsulated in **Agent Skills** (`.claude/skills/`).\n\n\n\n### **4. Non-Goals**\n\n* No payment processing.\n\n* No video hosting.\n\n\n\n**Output:** Create the file `specs/001-ai-native-book-platform/spec.md`."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Smart Auth & Onboarding (Priority: High)

As a new user, I want to sign up via GitHub so I can access personalized content.

**Why this priority**: Essential for user acquisition and personalized learning experience kickoff.

**Independent Test**: User can successfully sign up via GitHub and complete the onboarding modal, with profile data (including hardware info) persisted in the database.

**Acceptance Scenarios**:

1.  **Given** I am a new user,
    **When** I sign up via GitHub,
    **Then** I am redirected to a modal to capture programming proficiency, AI proficiency, and hardware background.
2.  **Given** I have provided all required information in the onboarding modal,
    **When** I submit the modal,
    **Then** my user profile is created in Neon DB with all 3 fields stored in the `additional_info` JSONB column.

---

### User Story 2 - The 4-Tab Lesson Interface (Priority: High)

As a student, I want to view lessons in different formats to suit my learning style.

**Why this priority**: Core learning experience and personalization feature.

**Independent Test**: A lesson page displays 4 tabs (Original, Summarize, Personalized, Urdu Translation), each showing the correct content.

**Acceptance Scenarios**:

1.  **Given** I am on a lesson page,
    **When** I view the lesson,
    **Then** I see four tabs: "Original", "Summarize", "Personalized", and "Urdu Translation".
2.  **Given** I am on a lesson page and the "Summarize" tab is selected,
    **When** the AI-generated bullet points are loaded (using `lesson-summarizer` skill),
    **Then** I see a summary of the lesson content.
3.  **Given** I am on a lesson page and the "Personalized" tab is selected,
    **When** the content is rewritten for my proficiency level (using `content-personalizer` skill),
    **Then** I see the personalized lesson content.
4.  **Given** I am on a lesson page and the "Urdu Translation" tab is selected,
    **When** the full lesson is translated to Urdu (using `urdu-translator` skill),
    **Then** I see the lesson content translated into Urdu.

---

### User Story 3 - Hybrid RAG Chatbot (Priority: Medium)

As a student, I want to ask questions about the book and get accurate answers.

**Why this priority**: Enhances the interactive learning experience with AI-powered Q&A.

**Independent Test**: A floating chatbot widget allows users to ask questions and receive context-aware answers from the AI.

**Acceptance Scenarios**:

1.  **Given** I am on a lesson page,
    **When** I activate the floating chatbot widget,
    **Then** I can type a question related to the book content.
2.  **Given** I have typed a question,
    **When** I submit the question,
    **Then** the system uses Google Gemini Embeddings for retrieval from Qdrant, and an OpenAI Agent generates an accurate response based on the retrieved context.
3.  **Given** I have selected text on the lesson page,
    **When** I use the context-menu option "Ask AI",
    **Then** the selected text is used as context for a chatbot query, and I receive an AI-generated answer.

---

### Edge Cases

- What happens when an AI skill fails to generate content (e.g., summarization, personalization, translation)? System should show original content or a fallback message.
- How does the system handle very long lesson content for summarization/personalization/translation? Ensure performance and responsiveness.
- What happens if the RAG chatbot retrieves irrelevant context? The OpenAI Agent should be robust enough to handle noise or indicate if it cannot answer confidently.

## Constitutional Alignment *(mandatory review)*

- [x] **Prime Directives**: Spec is consistent with `constitution.md` and `spec.md` as single sources of truth, adheres to SDD, and considers agentic workflows.
- [x] **Technology Mandates**: All technology choices (Frontend: Docusaurus v3, React, TypeScript, Tailwind CSS v3; Backend: FastAPI, Python 3.11+, `python-jose` for JWT, Neon Postgres, Qdrant Cloud; Auth: `better-auth` Client SDK for frontend, `python-jose` for backend JWT validation) align with the constitution's specified stack and versions.
- [x] **Functional Requirements (Bonus Constraints)**:
  - [x] Hardware info capture during onboarding (Auth & Profile) is specified.
  - [x] Urdu Translation via AI Skill (Localization) is specified.
  - [x] RAG with context-aware selection (Chatbot) is specified.
- [x] **Engineering Standards**: Code quality (Strict TypeScript for frontend, Pydantic models for backend), history/governance (PHR, ADR, folder hierarchy) are considered in the requirements.
- [x] **Failure Prevention**: Dependency lock and secrets management (using `.env`) are respected in the design.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST allow new users to sign up via GitHub.
- **FR-002**: Upon first login, the system MUST present a modal to capture Programming Proficiency (Beginner/Intermediate/Expert), AI Proficiency (Beginner/Intermediate/Expert), and Hardware Background (e.g., "RTX 3060, 16GB RAM").
- **FR-003**: The system MUST store the collected proficiency and hardware information in the `additional_info` JSONB column of the user's profile in Neon DB.
- **FR-004**: Each lesson page MUST display content in four distinct tabs: "Original", "Summarize", "Personalized", and "Urdu Translation".
- **FR-005**: The system MUST use the `lesson-summarizer` AI skill to generate bullet-point summaries for the "Summarize" tab.
- **FR-006**: The system MUST use the `content-personalizer` AI skill to rewrite lesson content based on the user's proficiency level for the "Personalized" tab.
- **FR-007**: The system MUST use the `urdu-translator` AI skill to provide a full Urdu translation of the lesson content for the "Urdu Translation" tab.
- **FR-008**: The system MUST provide a floating chatbot widget on lesson pages.
- **FR-009**: The chatbot MUST allow students to ask questions about the book content.
- **FR-010**: The chatbot MUST use Google Gemini Embeddings for vectorizing book content and user queries, storing/retrieving from Qdrant.
- **FR-011**: The chatbot MUST use an OpenAI Agent to generate responses based on retrieved context.
- **FR-012**: The system MUST support a context-menu option (e.g., select text -> "Ask AI") to integrate selected text directly into chatbot queries.

### Key Entities

- **User Profile**: Represents a student, including GitHub login, programming proficiency, AI proficiency, and hardware background (stored in `additional_info` JSONB).
- **Lesson**: Core educational content, available in original Markdown, AI-summarized, AI-personalized, and AI-translated (Urdu) formats.
- **Chatbot Interaction**: Represents a user's query and the AI's response, potentially linked to specific lesson context.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of new users successfully complete the GitHub signup and onboarding modal (including hardware info capture).
- **SC-002**: Lesson pages load all four content tabs within 3 seconds for 90% of users.
- **SC-003**: AI-generated content (summaries, personalized, Urdu translations) is available and displayed for 100% of lessons.
- **SC-004**: 90% of chatbot queries receive a relevant and accurate AI-generated response.
- **SC-005**: User satisfaction with personalized content and chatbot interactions, as measured by post-lesson surveys, averages 4 out of 5 stars or higher.
- **SC-006**: At least 75% of users engage with the personalized content or chatbot features during their learning sessions.

## Assumptions

- AI skills (`lesson-summarizer`, `content-personalizer`, `urdu-translator`) will be developed and integrated separately but are considered available for this feature.
- Google Gemini Embeddings and OpenAI Agent SDK integrations are robust and performant.
- Docusaurus provides sufficient extensibility for custom React components and tabbed interfaces.
- Existing GitHub OAuth infrastructure (if any) is compatible or can be adapted for user signup.
- Network connectivity and API access to external AI services (Google Gemini, OpenAI) are reliable.

## Non-Goals

- No payment processing.
- No video hosting.
