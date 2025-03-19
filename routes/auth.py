import uuid
import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from database import getdb
from model.user import User
from schema.user_create import UserCreate
from sqlalchemy.orm import Session

from schema.user_login import UserLogin


router = APIRouter()

@router.post("/signup",status_code=201) # ✅ Use POST method
def sign_up(user: UserCreate, db : Session = Depends(getdb)):
    # ✅ Corrected Query
    userdb = db.query(User).filter(User.email == user.email).first()

    if userdb:
        raise HTTPException(status_code=400, detail="User already exists")

    # ✅ Hash password correctly
    password_hash = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

    # ✅ Create User
    new_user = User(id=str(uuid.uuid4()), username=user.username, email=user.email, password=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()  # ✅ Close the session

    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}


@router.post("/login") # 
def login(user : UserLogin , db : Session = Depends(getdb)):
    # Check the existence of the user

    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        raise HTTPException(status_code=400, detail="No Data found for this email id")
    
    is_exists = bcrypt.checkpw(user.password.encode(), user_db.password)

    if not is_exists:
        raise HTTPException(status_code=400, detail="Invalid Password")
    
    if is_exists:
        return user_db
    # Check Password is Mathced or Not