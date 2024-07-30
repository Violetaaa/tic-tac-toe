import logging
from tictactoe.domain import model
from tictactoe.adapters.repository import AbstractRepository

logger = logging.getLogger(__name__)

def create(
    repo: AbstractRepository,
    session
) -> None:
    newMatch = model.initMatch()
    repo.create(newMatch)
    session.commit()
    logger.info(f"New match inserted: {newMatch}")
    return newMatch.id

def get_status(id, repo: AbstractRepository, session):
    logger.info(f"Get status for MatchId: {id}")
    match = repo.get(id)
    movements = repo.getAll(id)
    match.board = model.formatBoard(movements)     
    logger.info(f"Match: {match}")
    return match

def move(id: int, player: str, x: int, y: int, repo: AbstractRepository, session):
    newMove = model.Movement(None, match_id=id, player=player, x_square=x, y_square=y)
    repo.add(newMove)
    session.commit()
    logger.info(f"New move inserted: {newMove}")
    
    match = repo.get(id)
    movements = repo.getAll(id, "desc")
    logger.debug(f"Match {match.id} movements: {movements}")

    updatedMatch = model.setNewProps(match, movements)
    repo.update(updatedMatch)
    logger.info(f"Updated match: {match.id}")

    session.commit()
