from pymongo import ASCENDING

async def create_indexes(db):
    await db.drivers.create_index([("phone", ASCENDING)], unique=True)
