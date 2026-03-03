from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    score: int = Field(..., ge=0, le=100)


class StudentUpdate(BaseModel):
    score: int = Field(..., ge=0, le=100)


class StudentOut(BaseModel):
    name: str
    score: int
