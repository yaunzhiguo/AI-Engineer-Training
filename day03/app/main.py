from fastapi import FastAPI, HTTPException
from day03.app.schemas import StudentCreate, StudentUpdate, StudentOut
from day02.service import StudentService

app = FastAPI(title="Student API", version="0.1.0")

svc = StudentService()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/students", response_model=list[StudentOut])
def list_students():
    return [StudentOut(name=n, score=s) for n, s in svc.list_all()]

@app.get("/students/{name}", response_model=StudentOut)
def get_student(name: str):
    score = svc.query(name)
    if score is None:
        raise HTTPException(status_code=404, detail="student not found")
    return StudentOut(name=name, score=score)

@app.post("/students", response_model=StudentOut, status_code=201)
def create_student(payload: StudentCreate):
    ok = svc.add(payload.name, payload.score)
    if not ok:
        raise HTTPException(status_code=409, detail="student already exists")
    return StudentOut(name=payload.name, score=payload.score)

@app.put("/students/{name}", response_model=StudentOut)
def update_student(name: str, payload: StudentUpdate):
    ok = svc.update(name, payload.score)
    if not ok:
        raise HTTPException(status_code=404, detail="student not found")
    return StudentOut(name=name, score=payload.score)

@app.delete("/students/{name}")
def delete_student(name: str):
    ok = svc.delete(name)
    if not ok:
        raise HTTPException(status_code=404, detail="student not found")
    return {"message": "deleted successfully"}
