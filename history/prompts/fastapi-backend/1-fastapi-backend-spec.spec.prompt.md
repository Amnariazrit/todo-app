---
id: 1
title: fastapi-backend-spec
stage: spec
date: 2026-02-07
surface: agent
model: haiku-4-5-20251001
feature: fastapi-backend
branch: 003-fastapi-backend
user: DELL
command: /sp.specify
labels: ["spec", "backend", "fastapi", "todo"]
spec: specs/003-fastapi-backend/spec.md
ticket: null
adr: null
pr: null
files:
  - specs/003-fastapi-backend/spec.md
  - specs/003-fastapi-backend/checklists/requirements.md
tests: []
---

# Prompt History Record: fastapi-backend-spec

## Original Prompt

```
We are in Phase II of Hackathon II: Full-Stack Todo Web Application.

Focus: Generate ONLY the backend specification for speckit.specify (do NOT include frontend or UI details here).

Requirements from hackathon doc (Phase II backend):
- Backend: Python FastAPI
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL (use the provided DATABASE_URL)
- Authentication: Better Auth JWT verification (shared secret from .env BETTER_AUTH_SECRET)
- All endpoints require JWT, filter by authenticated user_id
- Implement Basic Level CRUD as REST API: GET /api/{user_id}/tasks, POST /api/{user_id}/tasks, GET /api/{user_id}/tasks/{id}, PUT /api/{user_id}/tasks/{id}, DELETE /api/{user_id}/tasks/{id}, PATCH /api/{user_id}/tasks/{id}/complete
- User isolation: Every operation MUST be limited to the authenticated user's tasks
- Use Pydantic for request/response models
- Use SQLModel for database models with user_id foreign key
- Environment variables: BETTER_AUTH_SECRET = "1Y5RelnIUhnK2CzYte3Oyk1TiX5FQBlX", BETTER_AUTH_URL = "http://localhost:3000", DATABASE_URL = "postgresql://neondb_owner:npg_grz1U5LxYRjD@ep-fancy-mud-a7nepf24-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
- Spec-Driven: All backend must map to tasks from speckit.tasks
- Integration with frontend: API client in frontend will send JWT in Authorization header; backend verifies and responds with JSON
- Error handling: 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Validation Error

Create a complete speckit.specify file focused ONLY on backend.

Structure it like this:
# speckit.specify
## Phase II – Backend Specification Only
### Todo Web App – FastAPI + SQLModel + Neon DB

### Context
- Phase: Phase II (Full-Stack Web)
- Prerequisite: Phase I console app completed
- Goal: Build secure, multi-user REST API backend that integrates successfully with frontend (Next.js)
- Stack: FastAPI, SQLModel, Pydantic, Neon PostgreSQL, PyJWT for token verification
- Auth: Better Auth JWT (verify signature with BETTER_AUTH_SECRET)
- DB: Use provided DATABASE_URL for Neon connection
- Spec-Driven: All features must be implemented via Claude Code from this spec → plan → tasks

### 1. Database Models
#### User Stories
- Backend stores users and tasks with proper relationships

#### Acceptance Criteria
- Users table (managed by Better Auth but mirrored in SQLModel): id (str, PK), email (str, unique), name (str), created_at (datetime)
- Tasks table: id (int, PK), user_id (str, FK to users.id), title (str, required), description (str, optional), completed (bool, default false), created_at (datetime, server_default=now()), updated_at (datetime, onupdate=now())
- Indexes: tasks.user_id, tasks.completed

### 2. Authentication & Security
#### User Stories
- Backend verifies JWT from frontend and enforces user isolation

#### Acceptance Criteria
- Dependency: get_current_user(token: str = Depends(OAuth2PasswordBearer)) → decode JWT with BETTER_AUTH_SECRET, extract user_id, return or raise 401/403
- All endpoints require this dependency
- Path param {user_id} must match token's user_id
- No token: 401 Unauthorized
- Mismatch: 403 Forbidden

### 3. API Endpoints (Basic CRUD)
#### User Stories
- Backend provides secure REST API for task management

#### Acceptance Criteria
- GET /api/{user_id}/tasks: List user's tasks (query params: status=all/pending/completed)
- POST /api/{user_id}/tasks: Create task (body: title str required, description str optional)
- GET /api/{user_id}/tasks/{id}: Get single task details
- PUT /api/{user_id}/tasks/{id}: Update task (body: title/description optional)
- DELETE /api/{user_id}/tasks/{id}: Delete task
- PATCH /api/{user_id}/tasks/{id}/complete: Toggle completed (no body)
- All responses: JSON with Pydantic models (TaskRead, TaskList)
- DB operations: Use SQLModel session via Depends, filter by user_id always
```

## Response Summary

Created a comprehensive backend specification for the todo web application following the requested structure. The specification includes:

1. Database Models section covering Users and Tasks tables with proper relationships
2. Authentication & Security section detailing JWT verification and user isolation requirements
3. API Endpoints section specifying all required CRUD operations
4. Additional sections covering user scenarios, functional requirements, success criteria, key entities, dependencies, and edge cases

The specification addresses all requirements from the hackathon document, focusing solely on backend functionality without including frontend or UI details. Created corresponding branch 003-fastapi-backend and spec file at specs/003-fastapi-backend/spec.md.

## Outcome

Successfully generated a complete backend specification that maps to the requirements provided, ready for the planning phase. The specification follows spec-driven development principles and maintains focus on user value and business needs without implementation details.

## Evaluation

The specification meets all requirements specified in the original prompt. It includes all required sections and addresses the core backend functionality needed for the todo web application including authentication, user isolation, and CRUD operations. The success criteria are measurable and technology-agnostic.