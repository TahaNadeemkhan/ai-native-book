# ADR-0001: Tech Stack Strategy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-11-28
- **Feature:** AI-Native Book Platform
- **Context:** The AI-Native Book Platform requires a robust and scalable technology stack for both frontend and backend development. The decision on the core technologies needs to ensure efficient development, maintainability, and alignment with project goals, including AI-driven personalization and translation.

## Decision

The core technology stack decisions are as follows:
- **Frontend Framework:** Docusaurus v3 (React, TypeScript)
- **Frontend Styling:** Tailwind CSS v3 (Strictly no v4)
- **Frontend Authentication:** `better-auth/react` Client SDK
- **Backend Framework:** FastAPI (Python 3.11+)
- **Backend Authentication Verification:** `python-jose` for JWT validation
- **Database:** Neon Postgres (SQLModel) with Multi-tenancy (`tenant_id` RLS)
- **Vector Database:** Qdrant Cloud
- **AI Integration:** LangChain/Google for Embeddings + OpenAI Agents SDK for Reasoning. All AI logic will be encapsulated in Agent Skills (`.claude/skills/`).

## Consequences

### Positive

- **Clear Separation of Concerns:** Docusaurus is optimized for content delivery and documentation, while FastAPI excels in building high-performance APIs for AI processing and data handling.
- **Modern Development Experience:** React, TypeScript, and FastAPI provide a modern and productive development environment.
- **Efficient Styling:** Tailwind CSS v3 offers a utility-first approach for rapid and consistent UI development.
- **Robust Authentication:** Decoupled authentication using `better-auth/react` on the frontend and `python-jose` for JWT verification on the backend ensures security and flexibility.
- **Scalable Data Management:** Neon Postgres with `tenant_id` RLS provides multi-tenancy support, and Qdrant Cloud offers a scalable solution for vector embeddings.
- **Powerful AI Capabilities:** The hybrid RAG model (Google Gemini for embeddings, OpenAI Agents for reasoning) leverages advanced AI for personalized content and intelligent chatbot functionality.
- **Reusable Intelligence:** Encapsulating AI logic in Agent Skills promotes reusability and maintainability.

### Negative

- **Learning Curve:** Developers unfamiliar with Docusaurus, FastAPI, SQLModel, or the specific AI frameworks might face an initial learning curve.
- **Integration Complexity:** Integrating various services and libraries (Docusaurus, FastAPI, Neon, Qdrant, LangChain, OpenAI) requires careful orchestration.
- **Dependency Management:** Strict adherence to Tailwind CSS v3 (no v4) and specific Python/TypeScript versions requires vigilant dependency management to prevent conflicts and ensure stability.
- **Vendor Lock-in:** Dependence on specific cloud services (Neon, Qdrant, Google Gemini, OpenAI) could lead to vendor lock-in.

## Alternatives Considered

- **Alternative Frontend Frameworks:**
    - **Next.js:** Considered for its full-stack capabilities, but Docusaurus was chosen for its strong focus on documentation and content-heavy applications, which aligns better with the platform's educational nature.
    - **Vue/Angular:** Evaluated, but React/TypeScript with Docusaurus provided the best fit for the content-centric platform.
- **Alternative Backend Frameworks:**
    - **Django:** Considered for its comprehensive ORM and admin interface, but FastAPI was chosen for its high performance, modern async support, and automatic OpenAPI documentation, which is ideal for an API-driven AI platform.
- **Alternative Authentication Solutions:**
    - **Full-stack authentication libraries (e.g., Auth0, Clerk for both frontend/backend):** Considered for simplicity, but the requirement for Python JWT verification with `python-jose` and the specific frontend `better-auth/react` SDK necessitated a decoupled approach.
- **Alternative AI/RAG Architectures:**
    - **Single LLM for both embedding and reasoning:** Considered for simplicity, but the hybrid approach (Google Gemini for embeddings, OpenAI Agents for reasoning) was chosen based on the instructor's recommendation for cost-efficiency and performance, leveraging the strengths of different models.

## References

- Feature Spec: `specs/001-ai-native-book-platform/spec.md`
- Implementation Plan: `specs/001-ai-native-book-platform/plan.md`
- Related ADRs: none
- Evaluator Evidence: none
