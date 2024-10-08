from datetime import datetime
from sqlalchemy import DateTime, Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from tictactoe.domain import model

mapper_registry = registry()
metadata = MetaData()

match = Table(
    "match",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("current_player", String(1)),
    Column("state", String(20)),
    Column("board", String(250)),
)

movement = Table(
    "movement",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("match_id", Integer, ForeignKey("match.id"), nullable=False),
    Column("player", String(1), nullable=False),
    Column("x_square", Integer, nullable=False),
    Column("y_square", Integer, nullable=False),
    Column("created_at", DateTime, default=datetime.now)
    )

def start_mappers():
    mapper_registry.map_imperatively(model.Movement, movement)
    mapper_registry.map_imperatively(model.Match, match)
