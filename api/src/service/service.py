from __future__ import annotations

from domain import model
from domain.model import Match
from adapters.repository import AbstractRepository

def create(
    repo: AbstractRepository,
    session
) -> None:
    newMatch = model.initMatch()
    repo.add(newMatch)
    session.commit()
    return newMatch.id

def get_status(id, repo: AbstractRepository, session):
    match = repo.get(id)
    session.commit()
    return match

def move():
    pass 