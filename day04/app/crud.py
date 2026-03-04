from sqlalchemy.orm import Session
from . import models, schemas

def get_student_by_name(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name == name).first()

def list_students(db: Session):
    return db.query(models.Student).order_by(models.Student.score.desc()).all()

def create_student(db: Session, data: schemas.StudentCreate):
    student = models.Student(name=data.name, score=data.score)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def update_student_score(db: Session, name: str, data: schemas.StudentUpdate):
    student = get_student_by_name(db, name)
    if not student:
        return None
    student.score = data.score
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, name: str) -> bool:
    student = get_student_by_name(db, name)
    if not student:
        return False
    db.delete(student)
    db.commit()
    return True
