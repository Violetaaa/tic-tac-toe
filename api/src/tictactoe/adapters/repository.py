import abc # abstract base classes
from tictactoe.domain import model 

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, match: model.Match):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> model.Match:
        raise NotImplementedError       
        
    @abc.abstractmethod
    def update(self, match: model.Match):
        raise NotImplementedError
    
    @abc.abstractmethod
    def add(self, match: model.Movement):
        raise NotImplementedError
    
    @abc.abstractmethod
    def getAll(self, id, order: str) -> list[model.Movement]:
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def create(self, match):
        self.session.add(match)

    def get(self, id):
        return self.session.query(model.Match).get(id)

    def update(self, match):
        self.session.query(model.Match).filter(model.Match.id == match.id).update({
            "current_player": match.current_player,
            "state": match.state
        })
    
    def getAll(self, id, order=None):
        match(order):
            case "desc":
                return self.session.query(model.Movement).filter(model.Movement.match_id == id).order_by(model.Movement.created_at.desc()).all()
            case _:
                return self.session.query(model.Movement).filter(model.Movement.match_id == id).all()

    def add(self, movement):
        self.session.add(movement)
