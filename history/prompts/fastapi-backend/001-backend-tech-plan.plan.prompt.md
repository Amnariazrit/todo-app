---
id: "001"
title: "Backend Tech Plan Generation"
stage: "plan"
date_iso: "2026-02-07"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "fastapi-backend"
branch: "003-fastapi-backend"
user: "user"
command: "sp.plan"
labels: ["backend", "architecture", "fastapi", "sqlmodel"]
spec: null
ticket: null
adr: null
pr: null
files_yaml:
  - "specs/003-fastapi-backend/speckit.plan"
tests_yaml: []
prompt_text: |
  We are in Phase II of Hackathon II: Full-Stack Todo Web Application.

  We already have the backend speckit.specify (FastAPI + SQLModel + Neon DB + Better Auth JWT).

  Now generate ONLY the backend technical plan in speckit.plan format.

  Focus: Detailed architecture, folder structure, models, dependencies, route implementation, security flow, migration strategy, and step-by-step build order for the secure, multi-user backend API.

  Key Requirements (must reflect in plan):
  - FastAPI async routes
  - SQLModel models (Task with user_id FK, timestamps server_default)
  - JWT verification dependency (PyJWT or fastapi-jwt-auth, use BETTER_AUTH_SECRET from .env)
  - User isolation: ALL queries filter by current_user.id
  - Endpoints: GET/POST/PUT/DELETE/PATCH as specified in spec
  - Pydantic schemas: TaskCreate, TaskRead, TaskUpdate, TaskList
  - DB connection: Use provided Neon DATABASE_URL
  - Error handling: 401, 403, 404, 422
  - Integration with frontend: Respond with JSON compatible with frontend api client (JWT header expected)
  - Environment: .env with BETTER_AUTH_SECRET, BETTER_AUTH_URL, DATABASE_URL

  Generate speckit.plan with this exact structure:

  # speckit.plan
  ## Phase II – Backend Technical Plan Only
  ### Todo Web App – FastAPI + SQLModel + Neon DB

  ### 1. Project Architecture Overview
  - FastAPI app structure (main.py, routers, dependencies, models)
  - Dependency injection flow (get_db, get_current_user)
  - Security & auth middleware plan

  ### 2. Folder Structure (Backend only)
  Detailed layout:
  - backend/
    - main.py
    - dependencies.py
    - models.py
    - schemas.py
    - routers/
      - tasks.py
    - db.py (engine, session)
    - migrations/ (Alembic)
    - config.py (settings from .env)

  ### 3. Database Setup & Models
  - SQLModel Task model with user_id: str (ForeignKey)
  - Timestamps: created_at, updated_at
  - Alembic migration strategy
  - Connection string from .env DATABASE_URL

  ### 4. Authentication & JWT Verification
  - get_current_user dependency
  - JWT decode with BETTER_AUTH_SECRET
  - User ID extraction & validation
  - Path param {user_id} match check

  ### 5. API Router & Endpoints Plan
  - APIRouter(prefix="/api/{user_id}")
  - Each endpoint:
    - Dependency: Depends(get_current_user), Depends(get_db)
    - Filter queries by current_user.id
    - Pydantic response_model
    - Status codes & exceptions

  ### 6. Pydantic Schemas
  - TaskCreate, TaskUpdate, TaskRead, TaskList
  - Exclude sensitive fields

  ### 7. Security & Integration Notes
  - How frontend JWT header is verified
  - User isolation enforcement
  - Error responses compatible with frontend

  ### 8. Implementation Order Recommendation
  Step-by-step:
  1. config & db setup
  2. models & schemas
  3. dependencies (get_db, get_current_user)
  4. tasks router & CRUD endpoints
  5. Migrations & testing

  ### 9. Non-Functional
  - Async where appropriate
  - Logging
  - Performance (indexes)
  - Testing plan (pytest)

  Generate the complete speckit.plan markdown content now — detailed, technical, and ready for @backend-engineer agent to implement.
  Make it full so backend integrates perfectly with frontend using provided .env secrets.
response_text: |
  # speckit.plan
  ## Phase II – Backend Technical Plan Only
  ### Todo Web App – FastAPI + SQLModel + Neon DB

  ### 1. Project Architecture Overview
  - **FastAPI app structure**: Main application entry point (main.py) orchestrates API routers, handles startup/shutdown events, manages global dependencies and exception handlers. Routers directory contains modularized API endpoints by domain (tasks), models define SQLModel entities with proper relationships and constraints, schemas define Pydantic models for request/response validation.
  - **Dependency injection flow**: `get_db()` dependency yields async SQLAlchemy session from engine pool, automatically managed by FastAPI lifecycle. `get_current_user()` dependency extracts JWT from Authorization header, decodes using BETTER_AUTH_SECRET, validates and extracts user_id for current request context.
  - **Security & auth middleware plan**: Built-in JWT verification dependency intercepts requests to protected endpoints, validates token signature and expiration, extracts user identity for request context. No additional middleware needed beyond FastAPI's native dependency system.

  ### 2. Folder Structure (Backend only)
  Detailed layout:
  ```
  backend/
  ├── main.py                 # FastAPI app instance, event handlers
  ├── dependencies.py         # get_db(), get_current_user() dependencies
  ├── models.py              # SQLModel Task model with user_id FK
  ├── schemas.py             # Pydantic models for validation (TaskCreate, etc.)
  ├── routers/
  │   └── tasks.py           # CRUD endpoints for /api/{user_id}/tasks/*
  ├── db.py                  # Database engine, session, connection logic
  ├── migrations/            # Alembic migration files
  └── config.py              # Settings from .env (DATABASE_URL, BETTER_AUTH_SECRET)
  ```

  ### 3. Database Setup & Models
  - **SQLModel Task model** with user_id: str (ForeignKey) to enforce user isolation at database level. Proper indexing on user_id for query performance. Field definitions: id (UUID), title (str, max_length=255), description (str, nullable), completed (bool, default=False), user_id (str, foreign_key), created_at (datetime, server_default), updated_at (datetime, server_default).
  - **Timestamps**: created_at uses `server_default=func.current_timestamp()` and updated_at uses `server_onupdate=func.current_timestamp()` for consistent database-level timestamp management.
  - **Alembic migration strategy**: Auto-generate migrations from model changes, ensure user_id foreign key constraint compatibility, test migration/reversion locally before deployment.
  - **Connection string**: Use provided Neon DATABASE_URL from environment variables with asyncpg driver for async operations.

  ### 4. Authentication & JWT Verification
  - **get_current_user dependency**: Extracts Authorization header, verifies "Bearer " prefix, passes JWT token to PyJWT decoder with BETTER_AUTH_SECRET from environment.
  - **JWT decode with BETTER_AUTH_SECRET**: Validates token signature, handles expiration, extracts payload containing user identity information.
  - **User ID extraction & validation**: Access user_id from JWT payload claims, verify exists and is properly formatted string, return validated user object for request context.
  - **Path param {user_id} match check**: Compare JWT-extracted user_id with path parameter user_id to prevent unauthorized access attempts between users (optional security hardening).

  ### 5. API Router & Endpoints Plan
  - **APIRouter(prefix="/api/{user_id}")**: All endpoints prefixed with user_id path parameter for clear isolation boundary.
  - **Each endpoint**:
    - Dependency: `Depends(get_current_user)` to ensure authentication, `Depends(get_db)` for database session
    - Filter queries by `current_user.id` or `user_id` parameter matching JWT claim
    - Pydantic response_model matching schemas (TaskRead, TaskList)
    - Standard status codes: 200 OK, 201 Created, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Validation Error
    - Exception handling with proper HTTPException raises for error conditions

  ### 6. Pydantic Schemas
  - **TaskCreate**: title (required), description (optional), completed (default False, ignored on create)
  - **TaskUpdate**: title (optional), description (optional), completed (optional) - all fields optional for partial updates
  - **TaskRead**: All Task model fields plus computed fields if needed, excludes sensitive data
  - **TaskList**: Paginated response structure with total count, list of TaskRead objects, pagination metadata
  - **Exclude sensitive fields**: Never expose database passwords, internal system fields, or user-sensitive data in public API responses

  ### 7. Security & Integration Notes
  - **Frontend JWT header verification**: Expect `Authorization: Bearer {token}` format from frontend API calls, standard for Better Auth integration.
  - **User isolation enforcement**: Critical security requirement - every query must filter by current_user.id, no exceptions. Use SQLAlchemy filters consistently across all operations.
  - **Error responses compatible with frontend**: JSON responses with consistent structure: `{error: string, message: string, code?: number}` for error handling, proper HTTP status codes that frontend can interpret.

  ### 8. Implementation Order Recommendation
  Step-by-step:
  1. **config & db setup**: Configure settings from .env, initialize async SQLAlchemy engine with Neon DATABASE_URL, create database dependency
  2. **models & schemas**: Define Task SQLModel with proper relationships and constraints, create Pydantic schemas for validation and serialization
  3. **dependencies**: Implement get_current_user with JWT verification using BETTER_AUTH_SECRET, create get_db dependency for session management
  4. **tasks router & CRUD endpoints**: Build GET/POST/PUT/DELETE/PATCH endpoints with proper authentication, authorization, validation, and response formatting
  5. **Migrations & testing**: Set up Alembic for database migrations, write pytest test suite covering all endpoints with mocked JWT tokens and isolated user data

  ### 9. Non-Functional
  - **Async where appropriate**: All FastAPI routes declared async, database operations use async SQLAlchemy with asyncpg driver for high concurrency
  - **Logging**: Structured logging for request/response cycles, authentication events, database operations, error tracking
  - **Performance**: Index user_id column for fast filtering, connection pooling for database operations, request/response validation performance optimization
  - **Testing plan**: Unit tests for models and schemas, integration tests for endpoints with real database connections, authentication flow testing with valid/invalid JWT tokens

  This technical plan provides the complete backend architecture for a secure, multi-user todo application with FastAPI, SQLModel, and Neon database integration. The implementation will follow FastAPI best practices while maintaining strict user isolation and JWT-based authentication flow compatible with the frontend requirements.
outcome: "Successfully generated comprehensive backend technical plan for FastAPI todo app with SQLModel, JWT authentication, and user isolation requirements. Plan is structured according to speckit.plan format and ready for implementation by backend engineer agent."
evaluation: "The generated plan covers all requested sections with detailed technical specifications, security considerations, and implementation order. It addresses all key requirements including async routes, user isolation, JWT verification, and proper error handling."
---
