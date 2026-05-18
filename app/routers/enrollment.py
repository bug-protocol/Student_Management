from fastapi import APIRouter

from Student_Management.app.services.enrollment_service import (
    enroll_student,
    get_enrollments
)

router = APIRouter()


@router.post("/enroll/{student_id}/{course_id}")
def enroll(student_id: str, course_id: str):
    return enroll_student(student_id, course_id)


@router.get("/enrollments")
def fetch_enrollments():
    return get_enrollments()