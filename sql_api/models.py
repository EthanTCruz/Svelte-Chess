from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    #current_games = relationship("Current_games", back_populates="owner")
    #past_games = relationship("Past_games", back_populates="owner")

class Current_games(Base):
    __tablename__ = "current_games"

    game_id = Column(String, primary_key=True, index=True)
    white_player_id = Column(String,ForeignKey("user.id"))
    black_player_id = Column(String,ForeignKey("user.id"))
    move_no = Column(Integer)
    pieces_and_positions = Column(String)
    turn = Column(String)

    #w_player = relationship("User", back_populates="current_games.white_player_id")
    #b_player = relationship("User", back_populates="current_games.black_player_id")


class Past_games(Base):
    __tablename__ = "past_games"

    game_id = Column(String, primary_key=True, index=True)
    white_player_id = Column(String,ForeignKey("user.id"))
    black_player_id = Column(String,ForeignKey("user.id"))
    move_no = Column(Integer)
    move = Column(String)
    game_status = Column(String)
    pieces_and_positions = Column(String)
    turn = Column(String)

    #w_player = relationship("User", back_populates="past_games.white_player_id")
    #b_player = relationship("User", back_populates="past_games.black_player_id")