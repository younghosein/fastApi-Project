import os
import time
from typing import Generator, Optional
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
#from fastapi.security import OAuth2PasswordBearer
from utils.OAuth2PasswordBearerWithCookie import OAuth2PasswordBearerWithCookie
from jose import jwt
from pydantic import ValidationError
from core import security
from core.config import settings
from db.session import SessionLocal
import schemas, models, crud
from schemas.token import TokenPayload

#AuthWithCookie:: https://www.fastapitutorial.com/blog/fastapi-jwt-httponly-cookie/
reuseable_oauth = OAuth2PasswordBearerWithCookie(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
    
def get_current_user(db: Session = Depends(get_db), token: str = Depends(reuseable_oauth)) -> schemas.user.User:
    try:
        #data = crud.logout.find_token(db=db, token=token)
        #if data:
        #    raise HTTPException(status_code=401, detail="توکن معتبر نیست")

        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        print(payload)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=401, detail="توکن معتبر نیست")
    
    _user = crud.user.get_user_by_id(db, user_id= token_data.sub)
    #crud.user.get(db, id=token_data.sub)
    if not _user:
        raise HTTPException(status_code=404, detail="کاربر پیدا نشد")
    print(_user)
    return _user

def get_current_eligible_user(current_user: schemas.user.User = Depends(get_current_user)) -> schemas.user.User:
    return current_user

'''
def Response(code, data):
    if code < 400 : 
        return JSONResponse(status_code=code, content={ "detail" : data })
    return HTTPException(status_code=code, detail=data)

def savefile(content, filename, subFolder=""):
    fn = time.strftime("%Y%m%d-%H%M%S")
    if subFolder != "":
        subFolder = subFolder+'/'
    try:
        os.makedirs(f"aismm/public/{subFolder}")
    except FileExistsError:
        pass
    media_path = f"public/{subFolder}{fn}_{filename}"
    with open("aismm/" + media_path, "wb") as f:
        f.write(content)
        
    return media_path
'''