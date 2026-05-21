import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import Student

from app.exceptions.custom_exceptions import (
    StudentNotFoundException,
    DuplicateStudentException
)


def create_student(db: Session, student_data):
    existing_student = db.query(Student).filter(
        Student.email == student_data.email
    ).first()

    if existing_student:
        raise DuplicateStudentException()
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


def get_all_students(
    db: Session,
    page: int = 1,
    limit: int = 10
):

    offset = (page - 1) * limit

    students = db.query(Student)\
        .offset(offset)\
        .limit(limit)\
        .all()

    return students


def get_student_by_id(db: Session, student_id: str):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise StudentNotFoundException()

    return student


def delete_student(db: Session, student_id: str):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise StudentNotFoundException()

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }