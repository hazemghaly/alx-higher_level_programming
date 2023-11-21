#!/usr/bin/python3
'''Write a script that lists all states from the database'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(City).all()
    for city in states:
        print("{}: {}".format(city.state.id, city.state.name))
        for city in city.state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
