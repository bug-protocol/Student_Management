from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class StudentResponse(BaseModel):

    id: str
    name: str
    email: EmailStr
    age: int

    class Config:
        from_attributes = True