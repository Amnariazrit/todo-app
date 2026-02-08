import asyncio
from db import create_tables

async def recreate_db():
    print("Recreating database tables...")
    await create_tables()
    print("Database tables created successfully!")

if __name__ == "__main__":
    asyncio.run(recreate_db())