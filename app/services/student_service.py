import uuid

from sqlalchemy.orm import Session

from Student_Management.app.database.models import Student


def create_student(db: Session, student_data):

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

    return db.query(Student).filter(Student.id == student_id).first()


def delete_student(db: Session, student_id: str):

    student = db.query(Student).filter(Student.id == student_id).first()

    if student:

        db.delete(student)

        db.commit()

    return student