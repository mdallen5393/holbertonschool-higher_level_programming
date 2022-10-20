#!/usr/bin/python3
"""
Script to list all states in the states table.
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state_name, city_id, city_name in session\
            .query(State.name, City.id, City.name)\
            .filter(City.state_id == State.id)\
            .order_by(City.id):
        print(f"{state_name}: ({city_id}) {city_name}")
