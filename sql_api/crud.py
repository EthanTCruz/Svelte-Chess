from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(user_id=user.user_id,username=user.username, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_current_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Current_games).offset(skip).limit(limit).all()


def create_user_game(db: Session, game: schemas.GameCreate, user_id: int):
    db_game = models.Item(**game.dict(), owner_id=user_id)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
