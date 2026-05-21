from fastapi import FastAPI

from app.database.connection import engine
from app.database.models import Base
from fastapi.middleware.cors import CORSMiddleware

from app.routers.student import router as student_router
from app.routers.course import router as course_router
from app.routers.enrollment import router as enrollment_router
from app.routers.auth_router import router as auth_router

from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.timing_middleware import TimingMiddleware

from app.exceptions.custom_exceptions import (
    StudentNotFoundException,
    CourseNotFoundException,
    DuplicateStudentException,
    DuplicateCourseException
)

from app.exceptions.exception_handlers import (
    student_not_found_handler,
    course_not_found_handler,
    duplicate_student_handler,
    duplicate_course_handler,
    generic_exception_handler
)

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(LoggingMiddleware)
app.add_middleware(TimingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

app.add_exception_handler(
    StudentNotFoundException,
    student_not_found_handler
)

app.add_exception_handler(
    CourseNotFoundException,
    course_not_found_handler
)

app.add_exception_handler(
    DuplicateStudentException,
    duplicate_student_handler
)

app.add_exception_handler(
    DuplicateCourseException,
    duplicate_course_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(student_router)
app.include_router(course_router)
app.include_router(enrollment_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message":"Working!!"}

@app.get("/health")
def health_check():
    return {"status": "OK"}