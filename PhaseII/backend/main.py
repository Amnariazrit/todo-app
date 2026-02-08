import sys
import os
# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import using absolute paths
from routers import tasks
from routers import auth
import db
import asyncio


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

# Include the routers
app.include_router(tasks.router)
app.include_router(tasks.legacy_router)  # For backward compatibility
app.include_router(auth.router)


@app.on_event("startup")
async def on_startup():
    await db.create_tables()


@app.get("/")
def read_root():
    return {"message": "Premium Todo API", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)