# Intelligence Record: Reusable Agent Skills

## Pattern: Agentic Skills (Reusable Intelligence)

- **Description**: Instead of hardcoding prompts inside Python/TypeScript code, we encapsulate AI logic into standalone Markdown
files ("Skills"). This decouples "Intelligence" from "Implementation".

- **Components**:
    1.  **Skill Definitions**: Located in `.claude/skills/<skill-name>/SKILL.md`.
    2.  **Skill Execution**: Backend reads these files and sends them as "System Instructions" to the OpenAI SDK.

- **Implemented Skills (Bonus Features)**:
    * **`content-personalizer`**: Rewrites content for Beginner/Expert levels.
    * **`urdu-translator`**: Translates content while preserving technical terminology.
    * **`lesson-summarizer`**: Extracts key bullet points from lessons.

- **Usage in Code**:
    * Backend (`ai_service.py`) loads the relevant `SKILL.md`.
    * Passes user input + Skill Prompt to LLM.
    * Returns structured output.

- **Benefits**:
    * **Zero-Code Updates**: Prompts can be improved without redeploying the backend.
    * **Consistency**: The same translation logic is reused across all endpoints.
    * **Compliance**: Meets the "Reusable Intelligence" Bonus Requirement.