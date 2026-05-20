from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.course_schema import (
    CourseCreate,
    CourseResponse
)

from app.services.course_service import (
    create_course,
    get_all_courses,
    get_course_by_id,
    delete_course
)

router = APIRouter()


@router.post("/courses", response_model=CourseResponse, status_code = 201)
def register_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return create_course(db, course)


@router.get("/courses", response_model=List[CourseResponse])
def fetch_courses(
    db: Session = Depends(get_db)
):
    return get_all_courses(db)


@router.get("/courses/{course_id}", response_model=CourseResponse)
def fetch_course(
    course_id: str,
    db: Session = Depends(get_db)
):
    return get_course_by_id(db, course_id)


@router.delete("/courses/{course_id}")
def remove_course(
    course_id: str,
    db: Session = Depends(get_db)
):
    return delete_course(db, course_id)