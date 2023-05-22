from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    password: str
    user_role: str

class Employee(BaseModel):
    id:int
    employee_name:str
    image_url: str
    id_role: int
    title_role: str
    last_login: Optional[datetime]


class Student(BaseModel):
    id: int
    student_name:str
    image_url:  Optional[str]
    id_field: int
    grade_field: str
    title_field: str
    field_manager: str    
    last_login: Optional[datetime]
