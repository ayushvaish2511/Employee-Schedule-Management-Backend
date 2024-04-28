
from motor.motor_asyncio import AsyncIOMotorClient

import urllib.parse

async def startup_db_client():
    """
    Connects to MongoDB using an async client and sets up the database connection.
    """
    try:
        username = urllib.parse.quote_plus('klsayushvaish')
        password = urllib.parse.quote_plus('Admin@123')

        uri = f"mongodb+srv://{username}:{password}@cluster0.tk979ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        db_client = AsyncIOMotorClient(uri)
        db = db_client['employeeDB']

        print("Successfully connected to MongoDB!")
        return db

    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise  


# if __name__ == '__main__':
#     startup_db_client()
