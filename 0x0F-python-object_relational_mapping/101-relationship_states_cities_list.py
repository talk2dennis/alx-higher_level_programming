#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the state table and get all her cities
    states = session.query(State)

    # prints the states
    for state in states:
        print(f"{state.id}: {state.name}")
        # prints the cities for each state
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
