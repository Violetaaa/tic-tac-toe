
from tictactoe.adapters import orm, repository
from flask_cors import CORS
import tictactoe.config as config
from tictactoe.service import service
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
    
    square = request.json["square"]
    x = square["x"]
    y = square["y"]

    service.move(
        request.json["matchId"],
        request.json["playerId"],
        x,
        y,
        repo,
        session
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
    return {"matchId": matchStatus.id, "status": matchStatus.state, "currentPlayer": matchStatus.current_player, "board": matchStatus.board}, 200
