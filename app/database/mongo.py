from typing import AsyncIterator
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


async def setup_mongo_db(
    conn_str: str, db_name: str
) -> AsyncIterator[AsyncIOMotorDatabase]:
    db_client = AsyncIOMotorClient(conn_str)
    db = db_client.get_database(db_name)

    yield db

    db_client.close()
