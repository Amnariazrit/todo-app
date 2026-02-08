# Premium Todo API - Backend

This is the backend service for the Premium Todo application, built with FastAPI and SQLModel.

## Features

- Secure JWT-based authentication using Better Auth
- Multi-user support with user isolation
- Full CRUD operations for tasks
- Task completion toggling
- Filtering and pagination support
- SQLModel for database modeling
- Async SQLAlchemy for database operations

## Prerequisites

- Python 3.9+
- PostgreSQL database (or Neon for cloud deployment)
- Better Auth for authentication

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with the following variables:
   ```env
   BETTER_AUTH_SECRET=your_better_auth_secret_here
   DATABASE_URL=postgresql+asyncpg://username:password@localhost/dbname
   BETTER_AUTH_URL=http://localhost:8000
   ```

5. Run the application:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

## API Endpoints

The API provides the following endpoints:

- `GET /api/{user_id}/tasks` - Get all tasks for a user (with optional filtering)
- `POST /api/{user_id}/tasks` - Create a new task for a user
- `GET /api/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a specific task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a specific task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle task completion status

## Authentication

All endpoints require a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

The user_id in the path parameter must match the user_id in the JWT token for security purposes.

## Filtering and Pagination

The GET /tasks endpoint supports the following query parameters:

- `status` - Filter by task status (all, pending, completed)
- `skip` - Number of records to skip (for pagination)
- `limit` - Maximum number of records to return (default: 100)

## Database

The application uses SQLModel with an async PostgreSQL database. The models are defined in `models.py`.

## Running Tests

To run the tests:

```bash
pytest tests/
```

## API Documentation

Interactive API documentation is available at:
- `/docs` - Swagger UI
- `/redoc` - ReDoc