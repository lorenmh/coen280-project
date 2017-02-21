from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .db import engine

Base = declarative_base()


class Subreddit(Base):
    __tablename__ = 'subreddit'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String)

    def __init__(self, name, url):
        self.name = name
        self.url = url


Base.metadata.create_all(engine)
