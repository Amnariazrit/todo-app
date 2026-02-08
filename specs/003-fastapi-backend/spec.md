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

### User Scenarios
- As an authenticated user, I can create new tasks associated with my account
- As an authenticated user, I can view all my tasks in a list
- As an authenticated user, I can view individual task details
- As an authenticated user, I can update my tasks
- As an authenticated user, I can delete my tasks
- As an authenticated user, I can mark tasks as complete/incomplete
- As a non-authenticated user, I cannot access any task data
- As a user, I should only see my own tasks, not other users' tasks

### Functional Requirements
1. Authentication System
   - The backend must validate JWT tokens sent in the Authorization header
   - The backend must extract the user_id from the validated JWT token
   - Invalid or missing tokens must result in 401 Unauthorized responses

2. User Isolation
   - Each API request must verify that the path parameter {user_id} matches the user_id from the JWT token
   - Users must only access their own data; any mismatch must result in 403 Forbidden
   - All database queries must filter by the authenticated user's ID

3. Task Management Endpoints
   - GET /api/{user_id}/tasks: Retrieve all tasks for the authenticated user with optional filtering by completion status
   - POST /api/{user_id}/tasks: Create a new task with title (required) and optional description
   - GET /api/{user_id}/tasks/{id}: Retrieve a specific task belonging to the authenticated user
   - PUT /api/{user_id}/tasks/{id}: Update an existing task belonging to the authenticated user
   - DELETE /api/{user_id}/tasks/{id}: Remove a task belonging to the authenticated user
   - PATCH /api/{user_id}/tasks/{id}/complete: Toggle the completion status of a task

4. Data Validation
   - Request bodies must be validated according to Pydantic model definitions
   - Invalid request data must result in 422 Validation Error responses
   - Required fields (e.g., title for new tasks) must be enforced

5. Response Format
   - All successful responses must return JSON data using Pydantic models
   - Proper HTTP status codes must be returned for all responses
   - Error responses must include descriptive error messages

### Success Criteria
- 100% of authenticated requests to task endpoints return appropriate JSON responses
- 100% of unauthenticated requests receive 401 Unauthorized responses
- 100% of requests attempting to access another user's data receive 403 Forbidden responses
- All CRUD operations complete within 2 seconds under normal load conditions
- Users can successfully perform all six core task operations (create, read list, read single, update, delete, toggle completion)
- Error handling follows the defined HTTP status code patterns (401, 403, 404, 422)

### Key Entities
- User: Identity entity represented by user_id extracted from JWT token
- Task: Core business entity with attributes: id, user_id, title, description, completed status, timestamps
- Authentication Token: JWT containing user identity information

### Dependencies and Assumptions
- The frontend will send properly formatted JWT tokens in the Authorization header
- The Better Auth secret (BETTER_AUTH_SECRET) will be available in environment variables
- The Neon PostgreSQL database will be accessible via the provided DATABASE_URL
- Pydantic and SQLModel libraries will be available for data modeling and validation
- FastAPI framework will be available for building the REST API

### Edge Cases
- Handling expired JWT tokens
- Requests with malformed JSON bodies
- Requests with missing required fields
- Requests to non-existent task IDs
- Requests to access another user's tasks (different user_id in path vs token)
- Database connectivity issues
- Concurrent access scenarios