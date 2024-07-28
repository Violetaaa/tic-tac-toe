import abc # abstract base classes
from domain import model 

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, match: model.Match):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> model.Match:
        raise NotImplementedError       
        
    @abc.abstractmethod
    def update(self, match: model.Match):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, match):
        self.session.add(match)

    def get(self, id):
        return self.session.query(model.Match).get(id)

    def update(self, match):
        self.session.query(model.Match).filter(model.Match.id == match.id).update({
            "current_player": match.current_player,
            "state": match.state
        })

