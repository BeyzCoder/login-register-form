from pydantic import BaseModel

class LoginForm(BaseModel):
    email: str
    password: str

class RegisterForm(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str