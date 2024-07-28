from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS

from .. import config
from adapters import orm, repository
from service import service

orm.start_mappers()

engine = create_engine(config.get_sqlite_uri(), echo=True)
orm.metadata.create_all(engine) # create tables if they don't exist

get_session = sessionmaker(bind=engine)

app = Flask(__name__)
CORS(app)

@app.route("/create", methods=["POST"])
def create_endpoint():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)

    matchId = service.create(
        repo,
        session,
    )
    return {"matchId": matchId}, 200


@app.route("/move", methods=["POST"])
def move_endpoint():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    
    movement = service.move(
        request.json["matchId"],
        request.json["playerId"],
        request.json["square.x"],
        request.json["square.y"],
        repo,
        session,
    )

    return "OK", 200


@app.route("/status/<int:matchId>", methods=["GET"]) 
def status_endpoint(matchId):
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)

    matchStatus = service.get_status(
        matchId,
        repo,
        session,
    )
    return {"matchId": matchStatus.id, "status": matchStatus.state, "currentPlayer": matchStatus.current_player, "board": ""}, 200
