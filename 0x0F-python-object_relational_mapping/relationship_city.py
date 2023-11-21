#!/usr/bin/python3
'''
module class city

'''


from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''class City '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship('State', back_populates='cities')
