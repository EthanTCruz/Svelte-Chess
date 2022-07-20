from typing import List, Union

from pydantic import BaseModel


class GameBase(BaseModel):
    move_no: int
    move: str
    game_status: str
    pieces_and_positions: str


class GameCreate(GameBase):
    pass


class Current_Game(GameBase):
    game_id: int
    white_player_id: int
    black_player_id: int
    turn: str

    class Config:
        orm_mode = True

class Past_Game(GameBase):
    game_id: int
    white_player_id: int
    black_player_id: int
    game_status: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    user_id: int
    username: str

class UserCheck(UserBase):
    username: str 
    password: str
    ok: bool = False 
    
    class Config:
        orm_mode=True



class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    username: str
    password: str
    #past_games: List[Past_Game] = []
    #current_games: List[Current_Game] = []

    class Config:
        orm_mode = True
