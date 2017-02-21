from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .engine import engine

Base = declarative_base()


class Subreddit(Base):
    __tablename__ = 'subreddit'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)

    def __init__(self, name, url):
        self.name = name


Base.metadata.create_all(engine)
