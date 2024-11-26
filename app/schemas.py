from pydantic import BaseModel, Field

class Driver(BaseModel):
    name: str
    phone: str = Field(..., pattern=r"^\+?\d{10,15}$")
    email: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "phone": "+1234567890",
                "email": "johndoe@example.com"
            }
        }
