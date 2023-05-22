from sqlalchemy.orm import Session
from schemas.user import User, Student, Employee
from sqlalchemy.sql import text
import json

class CRUDUser():
    def get_user_by_id(self, db:Session, user_id: int)-> User:
        if user_id:
            _user = db.execute(text(f'SELECT * FROM [dbo].[get_user_by_id] ({user_id})')).first()
            db.commit()
            return User(**json.loads(_user[0])[0])
        return None
    
    def get_student_display_info(self, db:Session, student_id: int)-> Student:
        if student_id:
            _student = db.execute(text(f'SELECT * FROM [dbo].[get_student_display_info] ({student_id})')).first()
            db.commit()
            if _student and _student[0]:
                return Student(**json.loads(_student[0])[0])
        return None

    def get_employee_display_info(self, db:Session, emp_id: int)-> Employee:
        if emp_id:
            _employee = db.execute(text(f'SELECT * FROM [dbo].[get_employee_display_info] ({emp_id})')).first()
            db.commit()
            if _employee and _employee[0]:
                return Employee(**json.loads(_employee[0])[0])
        return None

user= CRUDUser()