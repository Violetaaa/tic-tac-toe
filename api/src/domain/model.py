from dataclasses import dataclass
from typing import List

@dataclass(unsafe_hash=True)
class Movement:
    id: int
    match_id: int
    player: str
    x_square: int
    y_square: int

@dataclass(unsafe_hash=True)
class Match:
    id: int
    current_player: str
    state: str
    # board: List[str]

def initMatch() -> Match:
    return Match(None, state="init", current_player="x")
