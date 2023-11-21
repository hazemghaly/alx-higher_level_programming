#!/usr/bin/python3
'''Write a script that lists all states from the database'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import Base, City
''' Module For Connecting To MySQL database
'''

if __name__ == "__main__":
    '''ss'''
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    st = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).all()
    for State_name, City_id, City_name in st:
        print("{}: ({}) {}".format(State_name, City_id, City_name))
    session.close()
