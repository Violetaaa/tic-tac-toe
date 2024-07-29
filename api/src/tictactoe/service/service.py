from tictactoe.domain import model
from tictactoe.adapters.repository import AbstractRepository
import sys

def create(
    repo: AbstractRepository,
    session
) -> None:
    newMatch = model.initMatch()

    repo.create(newMatch)
    session.commit()
    return newMatch.id

def get_status(id, repo: AbstractRepository, session):
    match = repo.get(id)
    movements = repo.getAll(id)
    match.board = model.formatBoard(movements)
    return match

def move(id: int, player: str, x: int, y: int, repo: AbstractRepository, session):
    newMove = model.Movement(None, match_id=id, player=player, x_square=x, y_square=y)
    repo.add(newMove)
    
    match = repo.get(id)
    movements = repo.getAll(id)

    updatedMatch = model.setNewProps(match, movements)
    repo.update(updatedMatch)
    
    session.commit()
