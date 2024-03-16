#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()

    # close the session
    session.close()
