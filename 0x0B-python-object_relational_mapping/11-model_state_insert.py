#!/usr/bin/python3
"""
Script to list all states in the states table.
"""
from sqlalchemy.orm import sessionmaker
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

    session.add(State(name="Louisiana"))
    state = session.query(State)\
        .filter(State.name == "Louisiana")\
        .order_by(State.id)[-1]
    print(state.id)

    session.commit()
