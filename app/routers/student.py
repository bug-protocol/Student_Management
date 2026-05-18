from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Student_Management.app.database.connection import get_db

from Student_Management.app.schemas.student_schema import (
    StudentCreate,
    StudentResponse
)

from Student_Management.app.services.student_service import (
    create_student,
    get_all_students,
    get_student_by_id,
    delete_student
)

router = APIRouter()


@router.post("/students", response_model=StudentResponse)
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)


@router.get("/students", response_model=List[StudentResponse])
def fetch_students(
    db: Session = Depends(get_db)
):
    return get_all_students(db)


@router.get("/students/{student_id}", response_model=StudentResponse)
def fetch_student(
    student_id: str,
    db: Session = Depends(get_db)
):
    return get_student_by_id(db, student_id)


@router.delete("/students/{student_id}")
def remove_student(
    student_id: str,
    db: Session = Depends(get_db)
):
    return delete_student(db, student_id)