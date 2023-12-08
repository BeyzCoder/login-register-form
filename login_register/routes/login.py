import sys
import os

sys.path.append(os.getcwd())

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database.config import SessionLocal
from database.schemas.login_form import LoginForm, RegisterForm
from database.create_user import create_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
async def register(request: RegisterForm, db: Session=Depends(get_db)) -> JSONResponse:
    data = create_user(db, request)
    if data != None:
        obj = {"info" : data, "message" : "User account has been created!"}
        return JSONResponse(content=obj, status_code=status.HTTP_201_CREATED)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)