from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models  # 关键：确保建表时注册了 Student
from . import schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students", response_model=list[schemas.StudentOut])
def get_students(db: Session = Depends(get_db)):
    return crud.list_students(db)

@app.get("/students/{name}", response_model=schemas.StudentOut)
def get_student(name: str, db: Session = Depends(get_db)):
    student = crud.get_student_by_name(db, name)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students", response_model=schemas.StudentOut)
def add_student(data: schemas.StudentCreate, db: Session = Depends(get_db)):
    exist = crud.get_student_by_name(db, data.name)
    if exist:
        raise HTTPException(status_code=409, detail="Student already exists")
    return crud.create_student(db, data)

@app.put("/students/{name}", response_model=schemas.StudentOut)
def update_student(name: str, data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student = crud.update_student_score(db, name, data)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.delete("/students/{name}")
def delete_student(name: str, db: Session = Depends(get_db)):
    ok = crud.delete_student(db, name)
    if not ok:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "deleted"}
