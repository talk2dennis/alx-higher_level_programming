#!/usr/bin/python3
"""
 a python file that contains the class definition of a State and
    an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State: inherits from Base declarative class
           links to the MySQL table states
    Args:
        id (int): the id of the state
        name (string): name of the state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
