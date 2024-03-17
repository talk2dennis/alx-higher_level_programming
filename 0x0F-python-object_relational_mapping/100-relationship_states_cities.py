#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    Base.metadata.create_all(engine)
    # creates new state object
    state = State(name="California")
    # creates new city object
    city = City(name="San Francisco")
    # creates the relationship
    city.state = state
    # save changes and commit
    session.add(state)
    session.add(city)
    session.commit()

    """
    # prints the newly created state id
    print(state.id)
    """
    session.close()
