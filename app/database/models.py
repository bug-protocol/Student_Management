from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Student(Base):

    __tablename__ = "students"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)


class Course(Base):

    __tablename__ = "courses"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique = True, nullable=False)
    description = Column(String)
    duration = Column(String)

class User(Base):

    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, nullable=False)