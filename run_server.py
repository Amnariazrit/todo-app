import sys
import os
# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath('.'))

# Change to the backend directory
os.chdir('D:\\amna.riaz\\todo-app\\todo-app\\backend')

# Import and run the app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Premium Todo API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import the tasks router directly
from routers.tasks import router as tasks_router
app.include_router(tasks_router)

# Import db module to handle startup
from db import create_tables

@app.on_event("startup")
async def on_startup():
    await create_tables()

@app.get("/")
def read_root():
    return {"message": "Premium Todo API", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)