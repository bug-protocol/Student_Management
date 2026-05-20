from app.database.db import enrollments


def enroll_student(student_id: str, course_id: str):

    if student_id not in enrollments:
        enrollments[student_id] = []

    enrollments[student_id].append(course_id)

    return {
        "message": "Enrollment successful",
        "student_id": student_id,
        "courses": enrollments[student_id]
    }


def get_enrollments():
    return enrollments