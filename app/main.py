from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.routes import router
from pydantic import BaseModel

app = FastAPI()

# Include your existing routes
app.include_router(router)

# MongoDB connection setup
MONGO_DETAILS = "mongodb://localhost:27017"  # Replace with your MongoDB connection string if necessary
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.driver_database  # Replace with your database name
driver_collection = db.drivers  # Replace with your collection name

# Pydantic model for consistent response structure
class Driver(BaseModel):
    name: str
    phone: str
    email: str


@app.post("/driver/register")
async def register_driver(data: dict):
    """
    Endpoint to register a driver. Modify this as needed to save data to MongoDB.
    """
    # Save driver to MongoDB
    result = await driver_collection.insert_one(data)
    return {
        "message": "Driver registered",
        "data": {**data, "_id": str(result.inserted_id)},
    }


@app.get("/driver/{identifier}", response_model=Driver)
async def get_driver(identifier: str):
    """
    Fetch a driver by phone number or email from MongoDB.
    """
    # Query MongoDB for the driver
    driver = await driver_collection.find_one({"$or": [{"phone": identifier}, {"email": identifier}]})
    if driver:
        return {
            "name": driver["name"],
            "phone": driver["phone"],
            "email": driver["email"],
        }
    
    # Raise a 404 error if no match is found
    raise HTTPException(status_code=404, detail="Driver not found!")


@app.get("/")
def home():
    """
    Home route of the API.
    """
    return {"message": "Welcome to the Driver Registration API"}
