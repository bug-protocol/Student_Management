from fastapi import FastAPI

from app.database.connection import engine
from app.database.models import Base

from app.routers.student import router as student_router
from app.routers.course import router as course_router
from app.routers.enrollment import router as enrollment_router
from app.routers.auth_router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
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