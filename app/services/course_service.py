import uuid

from sqlalchemy.orm import Session

from Student_Management.app.database.models import Course


def create_course(db: Session, course_data):

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

    return db.query(Course).filter(Course.id == course_id).first()


def delete_course(db: Session, course_id: str):

    course = db.query(Course).filter(Course.id == course_id).first()

    if course:

        db.delete(course)

        db.commit()

    return course