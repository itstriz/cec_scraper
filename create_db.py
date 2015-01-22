import sqlite3 as lite
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///closings.db')

Base = declarative_base()

class Closings(Base):
    __tablename__ = 'closings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    closed = Column(Boolean)
    date = Column(Date)

class LastUpdate(Base):
    __tablename__ = 'last_update'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date)

Base.metadata.create_all(db)
