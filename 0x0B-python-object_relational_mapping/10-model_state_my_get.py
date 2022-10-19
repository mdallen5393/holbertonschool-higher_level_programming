#!/usr/bin/python3
"""
Script to list all states in the states table.
"""
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from model_state import Base, State
from sqlalchemy import (create_engine)
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State)\
            .order_by(State.id).filter(State.name == sys.argv[4]).one()
        print(state.id)
    except Exception:
        print("Not found")
