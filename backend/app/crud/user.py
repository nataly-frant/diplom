from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    fake_hashed_pw = "hashed_" + user.password
    db_user = User(username=user.username, email=user.email,
                   hashed_password=fake_hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
