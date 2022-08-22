from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    '*'
]




# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/create/current_games/", response_model=schemas.GameBase)
def create_game_for_user(
    game: schemas.GameBase, db: Session = Depends(get_db)
):
    return crud.create_user_game(db=db, game_data=game)

@app.post("/join/current_games/", response_model=schemas.GameJoin)
def create_game_for_user(
    user: schemas.UserBase, db: Session = Depends(get_db)
):
    game = crud.join_a_game(db=db, user=user)
    print(f"game object{game.game_id}")
    waiting_for_other_player = False
    if game.white_player_id == game.black_player_id:
        waiting_for_other_player=True
    color = "W"
    if int(game.black_player_id) == int(user.user_id):
        color = "B"
    print(color)
    game_data = schemas.GameJoin(game_id=game.game_id,white_player_id=game.white_player_id,
    black_player_id=game.black_player_id, waiting_for_other_player=waiting_for_other_player,
    pieces_and_positions=game.pieces_and_positions, player_color=color)
    return game_data


@app.post("/sign-in",response_model=schemas.UserCheck)
def validate_credentials(
    username: str, password: str, db: Session = Depends(get_db)
):

    db_user = crud.validate_credentials(db, username=username,password=password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db_user.ok = True
        return db_user



@app.get("/current_games/", response_model=List[schemas.Current_Game])
def read_current_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    current_games = crud.get_current_games(db, skip=skip, limit=limit)
    return current_games

@app.get("/current_games/board/{user_id}/{game_id}", response_model=schemas.GameBoard)
def get_current_game_board(user_id: int, game_id: int, db: Session = Depends(get_db)):
    game = schemas.GetGameBoard(user_id=user_id,game_id=game_id)
    print(game)
    game_board = crud.get_game_board(db=db, game=game)
    return game_board

@app.get("/current_games/board/{user_id}/{game_id}/{move}", response_model=schemas.GameBoard)
def move_piece(user_id: int, game_id: int,move: str, db: Session = Depends(get_db)):
    game = schemas.GetGameBoard(user_id=user_id,game_id=game_id)
    print(game)
    game_board = crud.move(db=db, game=game,move=move)
    return game_board


app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)