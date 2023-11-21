#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    st = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).all()
    for State.name, City.id, City.name in st:
        print("{}: ({}) {}".format(State.name, City.id, City.name))
    session.close()
