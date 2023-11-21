#!/usr/bin/python3
'''Write a script that lists all states from the database'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import Base, City

''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    try:
        cities = session.query(City).all()
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
