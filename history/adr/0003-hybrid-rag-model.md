# ADR-0003: Hybrid RAG Model

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-11-28
- **Feature:** AI-Native Book Platform
- **Context:** The AI-Native Book Platform requires a robust and efficient RAG (Retrieval-Augmented Generation) model to provide accurate and context-aware answers to user questions about the book content. The instructor has recommended a specific hybrid approach for cost-efficiency and performance.

## Decision

The RAG model will implement a hybrid approach:
- **Embeddings:** Google Gemini Embeddings will be used to vectorize book content during ingestion and user queries during retrieval.
- **Vector Storage:** Qdrant Cloud will store the vectorized book content.
- **Reasoning/Answer Generation:** OpenAI Agents SDK will be used to generate responses based on the context retrieved from Qdrant. All AI logic will be encapsulated in Agent Skills (`.claude/skills/`).

## Consequences

### Positive

- **Optimized Performance and Cost:** Leveraging Google Gemini for embeddings is often cost-effective, while OpenAI Agents are known for powerful reasoning capabilities, providing a balanced solution.
- **Instructor Alignment:** Directly follows the instructor's recommendation, ensuring compliance with project guidelines and potentially simplifying future reviews.
- **Scalable Vector Search:** Qdrant Cloud provides a highly scalable and efficient vector database for storing and retrieving book knowledge.
- **Modular AI Logic:** Encapsulating AI logic in Agent Skills promotes reusability, testability, and easier management of complex AI workflows.
- **Context-Aware Responses:** The RAG architecture ensures that AI-generated answers are grounded in the actual book content, reducing hallucinations and improving accuracy.

### Negative

- **Integration Complexity:** Integrating multiple AI services (Google Gemini, OpenAI, Qdrant) and a framework like LangChain adds a layer of complexity to the overall system design and implementation.
- **Dependency on External Services:** Reliance on external AI providers introduces potential points of failure, latency, and cost implications that need to be carefully managed.
- **Data Privacy Concerns:** Handling sensitive user queries and potentially private book content with external AI services requires careful consideration of data privacy and compliance.
- **Debugging Challenges:** Diagnosing issues in a multi-component AI pipeline can be complex, requiring tracing data flow across different services.

## Alternatives Considered

- **Using a single LLM for both embedding and reasoning (e.g., only OpenAI models, or only Google Gemini models):**
    - **Why rejected:** While simpler to integrate, this approach might not achieve the same level of cost-efficiency or specialized performance for both embedding and reasoning tasks as the hybrid model, as per the instructor's recommendation.
- **Using a self-hosted vector database (e.g., pgvector, FAISS):**
    - **Why rejected:** Qdrant Cloud was chosen for its managed service benefits, scalability, and ease of use, reducing operational overhead compared to self-hosting a vector database.
- **Implementing custom RAG logic without a framework like LangChain:**
    - **Why rejected:** LangChain provides a robust framework for building LLM applications, abstracting much of the complexity of integrating different components and offering established patterns for RAG, making development faster and more reliable.

## References

- Feature Spec: `specs/001-ai-native-book-platform/spec.md`
- Implementation Plan: `specs/001-ai-native-book-platform/plan.md`
- Related ADRs: `ADR-0001: Tech Stack Strategy`, `ADR-0002: Authentication Architecture`
- Evaluator Evidence: none
