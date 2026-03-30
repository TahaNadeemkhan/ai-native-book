# ADR-0002: Authentication Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-11-28
- **Feature:** AI-Native Book Platform
- **Context:** The AI-Native Book Platform requires a secure and efficient authentication system. Given the technology mandates (Better-Auth Client SDK for frontend, Python 3.11+, and `python-jose` for JWT validation on the backend), a decoupled authentication approach is necessary.

## Decision

The authentication architecture will be decoupled:
- **Frontend Authentication:** `better-auth/react` Client SDK will handle user sign-up and sign-in flows, including integration with GitHub OAuth.
- **Backend Authentication Verification:** The FastAPI backend will verify JWT tokens using `python-jose`. It will not use a `better-auth` Python SDK, as one is not available and the existing `python-jose` library is suitable for JWT validation.

## Consequences

### Positive

- **Enhanced Security:** Decoupling authentication logic between frontend and backend reduces attack surface and promotes independent security best practices for each layer.
- **Flexibility:** Allows for using the most suitable client-side authentication SDK (`better-auth/react`) while maintaining robust, standard JWT verification on the backend.
- **Alignment with Constraints:** Strictly adheres to the project's technology mandates, specifically using `better-auth/react` for the frontend and `python-jose` for backend JWT verification.
- **Clear Responsibility:** Clearly separates concerns, with the frontend managing user interaction and token acquisition, and the backend solely responsible for token validation and authorization.

### Negative

- **Increased Complexity:** Managing two distinct authentication components (frontend SDK and backend verification) might introduce more complexity compared to a single, monolithic authentication solution.
- **Potential for Misconfiguration:** Requires careful configuration and synchronization between the frontend and backend to ensure JWT issuance and validation work seamlessly.
- **Debugging Challenges:** Debugging authentication issues might require inspecting both frontend and backend logs and network traffic.
- **Dependency on `python-jose`:** The backend's reliance on `python-jose` means any vulnerabilities or limitations in this library would affect the entire system.

## Alternatives Considered

- **Using a unified authentication solution (e.g., Auth0, Firebase Auth with both frontend SDK and backend libraries):**
    - **Why rejected:** The project's specific requirement to use `better-auth/react` for the frontend and the absence of a direct Python SDK for `better-auth` led to the rejection of a fully unified third-party solution.
- **Implementing custom authentication logic on both frontend and backend:**
    - **Why rejected:** This would introduce significant development overhead, increase the risk of security vulnerabilities, and deviate from the use of established SDKs and libraries as mandated.
- **Using a different JWT library on the backend:**
    - **Why rejected:** `python-jose` is explicitly mandated by the project's constitution for JWT validation, ensuring consistency and adherence to defined standards.

## References

- Feature Spec: `specs/001-ai-native-book-platform/spec.md`
- Implementation Plan: `specs/001-ai-native-book-platform/plan.md`
- Related ADRs: `ADR-0001: Tech Stack Strategy`
- Evaluator Evidence: none
