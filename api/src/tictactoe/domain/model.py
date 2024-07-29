from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import sys

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
    return Match(None, state="init", current_player="x", board=None)

def setNewProps(match: Match, movements: list[Movement]) -> Match: 
    print("****************mov:" +str(movements), file=sys.stderr)
    match.state = updateState(movements)
    match.current_player = swichPlayer(movements[0].player)
    print("****************match:" +str(match), file=sys.stderr)
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
    return "ONGOING"

def populateBoard(movements: list[Movement]) -> list:
    board: list = [[None for _ in range(3)] for _ in range(3)]
    for move in movements:
        board[move.x_square][move.y_square] = move.player
    print("****************populateBoard:" +str(board), file=sys.stderr)
    return board

def findWinner(board: list) -> str:
    for c in WINNER_COMBINATIONS:
        if board[c[0][0]][c[0][1]] == board[c[1][0]][c[1][1]] == board[c[2][0]][c[2][1]]:
            return board[c[0][0]][c[0][1]]
    return None

def isBoardComplete(board: list) -> bool:
    for row in board:
        for square in row:
            if square is None:
                return False
    return True

def formatBoard(movements: list[Movement]) -> list[dict]:
    print("****************movs:" +str(movements), file=sys.stderr)
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