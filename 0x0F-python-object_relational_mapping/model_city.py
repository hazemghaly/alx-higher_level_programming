#!/usr/bin/python3
'''
model states
'''


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
'''
dd
'''
Base = declarative_base()


class State(Base):
    '''
    class
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
