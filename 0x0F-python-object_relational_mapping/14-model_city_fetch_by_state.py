#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py that prints all City objects
    from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database using join
    results = session.query(State, City).join(City)
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # close the session
    session.close()
