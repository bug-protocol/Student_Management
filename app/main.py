from fastapi import FastAPI

from Student_Management.app.database.connection import engine
from Student_Management.app.database.models import Base

from Student_Management.app.routers.student import router as student_router
from Student_Management.app.routers.course import router as course_router
from Student_Management.app.routers.enrollment import router as enrollment_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(student_router)
app.include_router(course_router)
app.include_router(enrollment_router)

@app.get("/")
def home():
    return {"message":"Working!!"}

@app.get("/health")
def health_check():
    return {"status": "OK"}