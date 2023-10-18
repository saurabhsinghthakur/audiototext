"""
Created By: Saurabh Singh
Date: 2023-10-17
"""
from motor.motor_asyncio import AsyncIOMotorClient

class Dao:
    """Dao"""
    def __init__(self) -> None:
        self.host = "127.0.0.1"
        self.port = "27017"
        self.database = "testdb"

    def conn(self):
        """Initiate Connection"""
        # MongoDB configuration
        mongo_uri = f"mongodb://{self.host}:{self.port}"
        client = AsyncIOMotorClient(mongo_uri)
        db = client[self.database]
        return db
