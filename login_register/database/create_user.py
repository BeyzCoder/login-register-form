import sys
import os

sys.path.append(os.getcwd())

from sqlalchemy.orm import Session

from database.models.user_accounts import User
from database.schemas.login_form import RegisterForm

def create_user(db: Session, form: RegisterForm) -> User:
    new_user_form = User(**form.__dict__)
    db.add(new_user_form)
    db.commit()
    db.refresh(new_user_form)
    return new_user_form