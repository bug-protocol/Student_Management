import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import Student


def create_student(db: Session, student_data):
    existing_student = db.query(Student).filter(
        Student.email == student_data.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=409,
            detail="Student with this email already exists"
        )
    student = Student(
        id=str(uuid.uuid4()),
        name=student_data.name,
        email=student_data.email,
        age=student_data.age
    )

    db.add(student)

    db.commit()

    db.refresh(student)

    return student


def get_all_students(db: Session):

    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: str):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


def delete_student(db: Session, student_id: str):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }