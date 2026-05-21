from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    StudentNotFoundException,
    CourseNotFoundException,
    DuplicateStudentException,
    DuplicateCourseException
)


async def student_not_found_handler(
    request: Request,
    exc: StudentNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "error": exc.message
        }
    )


async def course_not_found_handler(
    request: Request,
    exc: CourseNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "error": exc.message
        }
    )


async def duplicate_student_handler(
    request: Request,
    exc: DuplicateStudentException
):

    return JSONResponse(
        status_code=409,
        content={
            "error": exc.message
        }
    )


async def duplicate_course_handler(
    request: Request,
    exc: DuplicateCourseException
):

    return JSONResponse(
        status_code=409,
        content={
            "error": exc.message
        }
    )

async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error"
        }
    )