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
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            logger.debug(f"Winner found: {row[0]}")
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            logger.debug(f"Winner found: {board[0][col]}")
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        logger.debug(f"Winner found: {board[0][0]}")
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        logger.debug(f"Winner found: {board[0][2]}")
        return board[0][2]
    
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
