import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import Course


def create_course(db: Session, course_data):
    existing_course = db.query(Course).filter(
        Course.name == course_data.name
    ).first()

    if existing_course:
        raise HTTPException(
            status_code=409,
            detail="Course already exists"
        )
    
    course = Course(
        id=str(uuid.uuid4()),
        name=course_data.name,
        description=course_data.description,
        duration=course_data.duration
    )

    db.add(course)

    db.commit()

    db.refresh(course)

    return course


def get_all_courses(db: Session):

    return db.query(Course).all()


def get_course_by_id(db: Session, course_id: str):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


def delete_course(db: Session, course_id: str):

    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(
            status_code = 404,
            detail = "Course not found!"
        )
    

    db.delete(course)

    db.commit()

    return {
        "message" : "Course deleted successfully!"
    }