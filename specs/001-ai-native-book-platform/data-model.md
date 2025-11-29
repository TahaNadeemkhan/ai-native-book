# Data Model: AI-Native Book Platform

## Entities

### User Profile
- `id`: Unique identifier (Primary Key)
- `tenant_id`: Tenant identifier (for multi-tenancy, RLS)
- `email`: User's email address
- `additional_info`: JSONB type, storing:
  - `hardware`: (e.g., "RTX 3060, 16GB RAM")
  - `programming_proficiency`: (Beginner/Intermediate/Expert)
  - `ai_proficiency`: (Beginner/Intermediate/Expert)

### Lesson
- `id`: Unique identifier (Primary Key)
- `tenant_id`: Tenant identifier (for multi-tenancy, RLS)
- `content`: Original Markdown content of the lesson
- `summary`: AI-generated bullet points summary (Text)
- `is_summary_generated`: Boolean flag indicating if summary has been generated

### Personalized Content
- `id`: Unique identifier (Primary Key)
- `user_id`: Foreign Key referencing `User Profile.id`
- `lesson_id`: Foreign Key referencing `Lesson.id`
- `content`: Personalized lesson content rewritten for user's proficiency level

### Vectors (Qdrant Collection: `book_knowledge`)
- Managed via Qdrant API, storing vector embeddings of book content.
- The schema for this is internal to Qdrant and managed through its API, not directly in Neon Postgres.
