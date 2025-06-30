#!/usr/bin/python3
""" a script that prints the first State object
from the database hbtn_0e_6_usa"""
import re
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = argv[4]

    if (re.search('^[a-zA-Z]+$', state) is None):
        print('Please enter a valid name State')
        exit(1)

    states = session.query(State).filter(State.name.like(state))

if states.count() == 0:
    print('Not found')
else:
    for state in states:
        print(state.id)
