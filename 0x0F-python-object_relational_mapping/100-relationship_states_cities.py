#!/usr/bin/python3
'''Write a script that lists all states from the database'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import  Base, City
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    california = State(name="California")
    session.add(california)
    session.commit()
    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.commit()
    states = session.query(State).all()
    session.close()
