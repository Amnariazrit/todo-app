# tasks.md
## FastAPI Todo Backend Implementation
### Phase II – Backend Implementation Tasks

## Phase 1: Setup & Configuration
- [X] T001 Initialize project structure with backend/ directory per plan
- [X] T002 Create requirements.txt with FastAPI, SQLModel, Pydantic, python-jose[cryptography], uvicorn, psycopg2-binary, alembic
- [X] T003 Create .env file with BETTER_AUTH_SECRET, DATABASE_URL, BETTER_AUTH_URL placeholders
- [X] T004 Create config.py with Settings class loading from .env

## Phase 2: Foundational Components
- [X] T005 Create db.py with async SQLAlchemy engine and session dependencies
- [X] T006 Set up SQLModel database connection using provided DATABASE_URL
- [X] T007 Create models.py file with Task SQLModel as specified
- [X] T008 Create schemas.py file with Pydantic models (TaskCreate, TaskUpdate, TaskRead, TaskList)
- [X] T009 Create dependencies.py with get_db() and get_current_user() dependencies
- [X] T010 Create main.py FastAPI app with proper startup configuration
- [X] T011 Initialize migrations/ directory with Alembic configuration

## Phase 3: [US1] Authentication & Security Implementation
**User Story**: Backend verifies JWT from frontend and enforces user isolation
**Independent Test Criteria**: All endpoints reject unauthorized requests with 401/403 status codes

- [X] T012 [P] [US1] Implement JWT verification in get_current_user dependency using BETTER_AUTH_SECRET
- [X] T013 [P] [US1] Extract user_id from JWT token payload and validate token signature
- [X] T014 [US1] Implement OAuth2PasswordBearer for token extraction from Authorization header
- [X] T015 [US1] Add user_id path parameter validation against JWT user_id for security
- [X] T016 [US1] Handle invalid/missing token scenarios with proper 401 responses
- [X] T017 [US1] Implement user isolation by filtering all queries with current_user.id
- [X] T018 [US1] Test authentication flow with mock JWT tokens

## Phase 4: [US2] Task Management Endpoints - Core CRUD
**User Story**: Backend provides secure REST API for task management
**Independent Test Criteria**: All basic CRUD operations (GET/POST/PUT/DELETE) work for authenticated users

- [X] T019 [P] [US2] Create tasks router with APIRouter(prefix="/api/{user_id}") structure
- [X] T020 [P] [US2] Implement GET /api/{user_id}/tasks endpoint with user_id filter
- [X] T021 [P] [US2] Implement POST /api/{user_id}/tasks endpoint for task creation
- [X] T022 [US2] Implement GET /api/{user_id}/tasks/{id} endpoint for single task retrieval
- [X] T023 [US2] Implement PUT /api/{user_id}/tasks/{id} endpoint for task updates
- [X] T024 [US2] Implement DELETE /api/{user_id}/tasks/{id} endpoint for task deletion
- [X] T025 [US2] Add Pydantic response models to all endpoints for proper serialization
- [X] T026 [US2] Add proper HTTP status codes (200, 201, 204, 404) to endpoints
- [X] T027 [US2] Test basic CRUD operations with valid authentication tokens

## Phase 5: [US3] Task Completion Toggle Endpoint
**User Story**: Backend provides endpoint to toggle task completion status
**Independent Test Criteria**: PATCH endpoint successfully toggles completed status for authenticated user

- [X] T028 [US3] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint for toggle functionality
- [X] T029 [US3] Verify user_id match between path parameter and JWT token for completion toggle
- [X] T030 [US3] Test completion toggle endpoint with various scenarios
- [X] T031 [US3] Ensure toggle only affects tasks belonging to authenticated user

## Phase 6: [US4] Data Validation & Error Handling
**User Story**: Backend validates all input and returns proper error responses
**Independent Test Criteria**: Invalid requests receive appropriate error responses with descriptive messages

- [X] T032 [P] [US4] Add Pydantic validation to TaskCreate schema (title required)
- [X] T033 [P] [US4] Add Pydantic validation to TaskUpdate schema (optional fields)
- [X] T034 [US4] Handle 422 validation errors with descriptive messages
- [X] T035 [US4] Implement proper exception handling for non-existent resources (404)
- [X] T036 [US4] Handle database constraint violations appropriately
- [X] T037 [US4] Add request/response validation middleware if needed
- [X] T038 [US4] Test validation and error handling scenarios

## Phase 7: [US5] Advanced Features & Filtering
**User Story**: Backend supports optional filtering and advanced task operations
**Independent Test Criteria**: GET endpoint supports status filtering (all/pending/completed)

- [X] T039 [US5] Add query parameters support to GET /api/{user_id}/tasks (status filter)
- [X] T040 [US5] Implement status filtering logic (all/pending/completed)
- [X] T041 [US5] Add pagination support to task listing endpoint
- [X] T042 [US5] Test filtering functionality with various scenarios

## Phase 8: [US6] Security Hardening & Integration
**User Story**: Backend enforces all security requirements and integrates properly with frontend
**Independent Test Criteria**: All security measures are in place and frontend integration works

- [X] T043 [US6] Implement additional security checks (user_id path vs token validation)
- [X] T044 [US6] Ensure all responses are JSON-compatible with frontend expectations
- [X] T045 [US6] Add structured logging for security events and operations
- [X] T046 [US6] Validate all endpoints follow proper security patterns
- [X] T047 [US6] Test edge cases and potential security bypasses

## Phase 9: Testing & Quality Assurance
- [X] T048 Create test suite with pytest for all endpoints
- [X] T049 Implement database fixture for testing with proper isolation
- [X] T050 Add authentication mocking for endpoint testing
- [X] T051 Run full test suite covering all user scenarios
- [X] T052 Verify all success criteria from spec are met
- [X] T053 Test edge cases and error conditions

## Phase 10: Polish & Documentation
- [X] T054 Add API documentation with FastAPI automatic docs
- [X] T055 Update README with backend setup and usage instructions
- [X] T056 Final integration testing with frontend API calls
- [X] T057 Performance testing to ensure 2-second response times
- [X] T058 Code cleanup and documentation improvements

## Dependencies

### User Story Completion Order:
- US1 must be completed before US2, US3, US4, US5, US6 (Authentication foundation required)
- US2 must be completed before US3 (Core CRUD required for completion toggle)
- US4, US5, US6 can proceed in parallel after US2 (Advanced features)

### Parallel Execution Examples per User Story:
- US2: GET, POST endpoints can be developed in parallel (T020, T021 are [P] tasks)
- US4: Schema validations can be done in parallel (T032, T033 are [P] tasks)

## Implementation Strategy
1. **MVP Scope**: Complete Phase 1, 2, 3, and US2 (basic authenticated CRUD) - T001 through T027
2. **Incremental Delivery**: Add US3, US4, US5, US6 as separate increments
3. **Quality Assurance**: End with testing, polish, and documentation phases