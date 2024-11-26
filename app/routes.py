from fastapi import APIRouter, HTTPException
from app.database import db
from app.schemas import Driver

router = APIRouter()

@router.post("/register")
async def register_driver(driver: Driver):
    driver_data = driver.dict()
    try:
        await db.drivers.insert_one(driver_data)
        return {"message": "Driver registered successfully!"}
    except Exception:
        raise HTTPException(status_code=400, detail="Driver already exists!")

@router.get("/driver/{phone}")
async def get_driver(phone: str):
    driver = await db.drivers.find_one({"phone": phone})
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found!")
    driver.pop("_id")  # Remove MongoDB's ObjectID from the response
    return driver
