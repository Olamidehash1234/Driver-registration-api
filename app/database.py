from motor.motor_asyncio import AsyncIOMotorClient

# Update with your correct MongoDB URI
MONGO_URI = "mongodb://localhost:27017"  # Local MongoDB
# MONGO_URI = "mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true&w=majority"  # MongoDB Atlas

client = AsyncIOMotorClient(MONGO_URI)
db = client.driver_registration
