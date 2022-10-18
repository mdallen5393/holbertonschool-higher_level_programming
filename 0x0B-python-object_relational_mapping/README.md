# PROJECT: 0x0B. Python - Object-relational mapping
### AUTHOR: Matthew Allen

## TASKS:
### 0. Get all states - 0-select_states.py
Script that lists all `states` from the database `hbtn_0e_0_usa`.

### 1. Filter states - 1-filter_states.py
Script that lists all `states` with a `name` starting with `N` from the database `hbtn_0e_0_usa`.

### 2. Filter states by user input - 2-my_filter_states.py
Script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

### 3. SQL Injection... - 3-my_safe_filter_states.py
Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.  But this time, write one that is safe from MySQL injections!

### 4. Cities by states - 4-cities_by_state.py
Script that lists all `cities` from the database `hbtn_0e_4_usa`.

### 5. All cities by state - 5-filter_cities.py
Script that takes in the name of the state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`.

### 6. First state model - model_state.py
Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.

### 7. All states via SQLAlchemy - 7-model_state_fetch_all.py
Script that lists all `State` objects from the database `hbtn_0e_6_usa`.

### 8. First state - 8-model_state_fetch_first.py
Script that prints the first `State` object from the database `hbtn_0e_6_usa`.

### 9. Contains `a` - 9-model_state_filter_a.py
Script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.

### 10. Get a state - 10-model_state_my_get.py
Script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`.

### 11. Add a new state - 11-model_state_insert.py
Script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.

### 12. Update a state - 12-model_state_update_id_2.py
Script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.

### 13. Delete states - 13-model_state_delete_a.py
Script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

### 14. Cities in state - model_city.py, 14-model_city_fetch_by_state.py
Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.  Script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`.
