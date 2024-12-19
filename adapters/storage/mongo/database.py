from typing import AsyncIterator
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


async def setup_mongo_db(
    conn_str: str, db_name: str
) -> AsyncIterator[AsyncIOMotorDatabase]:
    """
    Sets up a connection to a MongoDB database, initialize beanie ODM and
    yields the database object.

    Args:
        conn_str (str): The connection string for the MongoDB server.
        db_name (str): The name of the database to connect to.

    Yields:
        AsyncIOMotorDatabase: The database object.

    Closes the database client after the resource usage is complete.
    """

    db_client = AsyncIOMotorClient(conn_str)
    db = db_client.get_database(db_name)

    await init_beanie(
        db,
        document_models=[
            "adapters.storage.mongo.repositories.order.OrderDocument",
        ],
    )

    yield db

    db_client.close()
