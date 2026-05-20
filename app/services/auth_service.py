import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import User

from app.auth.password_handler import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import create_access_token


def register_user(db: Session, user_data):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

    user = User(
        id=str(uuid.uuid4()),
        email=user_data.email,
        password=hash_password(user_data.password),
        role=user_data.role
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "User registered successfully"
    }


def login_user(db: Session, login_data):

    user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        login_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }