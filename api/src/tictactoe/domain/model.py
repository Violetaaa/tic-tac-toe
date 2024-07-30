from dataclasses import dataclass
from datetime import datetime
import logging
from typing import Optional

logger = logging.getLogger(__name__)

@dataclass(unsafe_hash=True)
class Movement:
    id: int
    match_id: int
    player: str
    x_square: int
    y_square: int
    created_at: Optional[datetime] = None

@dataclass(unsafe_hash=True)
class Match:
    id: int
    current_player: str
    state: str
    board: list

class InvalidMovement(Exception):
    pass
    # TODO

def initMatch() -> Match:
    return Match(None, state="INIT", current_player="x", board=None)

def setNewProps(match: Match, movements: list[Movement]) -> Match: 
    logger.debug(f"Movements order by created_at desc: {movements}")
    match.state = updateState(movements)
    match.current_player = swichPlayer(movements[0].player)
    logger.debug(f"Last player: {movements[0].player} - next player: {match.current_player}")
    logger.debug(f"Updated match: {match}")
    return match

def swichPlayer(player: str) -> str:
    return "o" if player == "x" else "x"

def updateState(movements: list[Movement]) -> str:
    board = populateBoard(movements)
    winner = findWinner(board)
    if winner:
        return f"{winner} WIN"
    if isBoardComplete(board):
        return "DRAW"
    return "ON GOING"

def populateBoard(movements: list[Movement]) -> list:
    board: list = [[None for _ in range(3)] for _ in range(3)]
    for move in movements:
        board[move.x_square-1][move.y_square-1] = move.player
    logger.debug(f"Populated board: {board}")
    return board

def findWinner(board: list) -> str:
    for c in WINNER_COMBINATIONS:
        if board[c[0][0]][c[0][1]] == board[c[1][0]][c[1][1]] == board[c[2][0]][c[2][1]]:
            winner = board[c[0][0]][c[0][1]]
            logger.debug(f"Winner found: {winner}")
            return winner
    return None

def isBoardComplete(board: list) -> bool:
    for row in board:
        for square in row:
            if square is None:
                return False
    return True

def formatBoard(movements: list[Movement]) -> list[dict]:
    logger.debug(f"Movements: {movements}")
    board = populateBoard(movements)
    formattedBoard = []
    for row in range(3):
        for col in range(3):
            formattedBoard.append({
                "row": row + 1,
                "col": col + 1,
                "value": board[row][col] or ""  
            })
    return formattedBoard


WINNER_COMBINATIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]
