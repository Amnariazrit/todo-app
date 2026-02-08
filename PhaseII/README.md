# Phase II - Fullstack Todo App

This phase contains the full-stack Todo application with a React frontend and FastAPI backend.

## Backend Features
- Secure JWT-based authentication using Better Auth
- Multi-user support with user isolation
- Full CRUD operations for tasks
- Task completion toggling functionality
- Filtering and pagination support
- SQLModel for database modeling
- Async SQLAlchemy for database operations

## Frontend Features
- Two frontend implementations:
  1. React-based SPA with Vite (in main frontend directory)
  2. Next.js application (in `app/` directory)

## Backend Structure
- `main.py` - FastAPI app instance with CORS middleware
- `config.py` - Settings configuration with environment variable loading
- `db.py` - Async SQLAlchemy engine and session management
- `models.py` - SQLModel database models (Task, User)
- `schemas.py` - Pydantic models for request/response validation
- `dependencies.py` - Authentication and database dependencies
- `routers/` - API route definitions
  - `tasks.py` - Task management endpoints
  - `auth.py` - Authentication endpoints

## Frontend Structure (React/Vite)
- `package.json` - Project dependencies and scripts
- `vite.config.js` - Vite configuration with proxy settings
- `public/index.html` - Main HTML file
- `src/App.js` - Main application component
- `src/index.js` - Application entry point
- `src/components/` - Reusable UI components
  - `TodoList.js` - Todo list component
- `src/pages/` - Page components
  - `Home.js` - Home page
  - `Login.js` - Login page
  - `Register.js` - Registration page
- `src/utils/api.js` - API utility functions
- `components/` - Additional UI components
- `hooks/` - Custom React hooks
- `lib/` - Utility libraries
- `styles/` - CSS stylesheets
- `tsconfig.json` - TypeScript configuration

## Frontend Structure (Next.js)
- `app/layout.tsx` - Root layout component
- `app/page.tsx` - Landing page
- `app/auth/page.tsx` - Authentication page
- `app/dashboard/page.tsx` - Dashboard page
- `app/login/page.tsx` - Login page
- `app/signup/page.tsx` - Signup page

## Setup Instructions

### Backend
1. Navigate to the backend directory: `cd PhaseII/backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with required variables
4. Run the server: `uvicorn main:app --reload`

### Frontend
1. Navigate to the frontend directory: `cd PhaseII/frontend`
2. Install dependencies: `npm install`
3. Run the development server: `npm run dev`