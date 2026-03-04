from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    score: int

class StudentUpdate(BaseModel):
    score: int

class StudentOut(BaseModel):
    name: str
    score: int

    class Config:
        from_attributes = True  # Pydantic v2
