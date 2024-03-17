#!/usr/bin/python3
"""
 a python file that contains the class definition of a City and
    an instance Base = declarative_base()
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City: inherits from Base declarative class
           links to the MySQL table states
    Args:
        id (int): the id of the state
        states.id (int): foreign key to State
        name (string): name of the state
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
