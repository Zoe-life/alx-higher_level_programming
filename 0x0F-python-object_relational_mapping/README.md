# Python Object Relational Mapping

## Overview

Database-focused exercises using raw SQL, MySQLdb, and SQLAlchemy to connect Python applications with relational data.

## Learning Objectives

- Write SQL scripts for schema creation and data retrieval.
- Connect Python scripts to MySQL databases.
- Query and filter records securely from Python.
- Use SQLAlchemy models and relationships to structure ORM code.

## Key Deliverables

- `0-select_states.py`
- `0-select_states.sql`
- `1-filter_states.py`
- `10-model_state_my_get.py`
- `100-relationship_states_cities.py`
- `100-relationship_states_cities.sql`
- `101-relationship_states_cities_list.py`
- `101-relationship_states_cities_list.sql`
- `102-relationship_cities_states_list.py`
- `11-model_state_insert.py`
- `12-model_state_update_id_2.py`
- `13-model_state_delete_a.py`
- `14-model_city_fetch_by_state.py`
- `14-model_city_fetch_by_state.sql`
- `2-my_filter_states.py`
- `3-my_safe_filter_states.py`
- `4-cities_by_state.py`
- `4-cities_by_state.sql`
- `5-filter_cities.py`
- `6-model_state.py`
- `6-model_state.sql`
- `7-model_state_fetch_all.py`
- `7-model_state_fetch_all.sql`
- `8-model_state_fetch_first.py`
- `9-model_state_filter_a.py`
- `model_city.py`
- `model_state.py`
- `relationship_city.py`
- `relationship_state.py`

## Requirements

- Python 3
- MySQL server
- MySQLdb
- SQLAlchemy

## Usage

Run SQL scripts in MySQL and execute Python programs with `python3 <filename>.py <username> <password> <database>` as required by the individual task.

## Detailed File Guide

- `0-select_states.sql` — SQL script listing all states in table.
- `0-select_states.py` — Python/MySQLdb script listing all states.
- `1-filter_states.py` — Lists states starting with letter `N`.
- `2-my_filter_states.py` — Filters states by name from CLI input (unsafe version).
- `3-my_safe_filter_states.py` — Safe parameterized filter for state lookup.
- `4-cities_by_state.sql` — SQL script joining cities and states.
- `4-cities_by_state.py` — Python version printing cities grouped by state.
- `5-filter_cities.py` — Prints cities for a provided state name.
- `6-model_state.sql` — SQL setup for ORM `states` model table.
- `6-model_state.py` / `model_state.py` — SQLAlchemy `State` model definition.
- `7-model_state.sql` — SQL verification query for ORM states table.
- `7-model_state_fetch_all.py` — Fetches all `State` rows using SQLAlchemy session.
- `8-model_state_fetch_first.py` — Fetches first `State` row.
- `9-model_state_filter_a.py` — Filters ORM states containing `a`.
- `10-model_state_my_get.py` — Retrieves state by exact name through ORM.
- `11-model_state_insert.py` — Inserts new state row via ORM.
- `12-model_state_update_id_2.py` — Updates state with ID 2.
- `13-model_state_delete_a.py` — Deletes states containing `a`.
- `14-model_city_fetch_by_state.sql` — SQL join query for cities and states.
- `14-model_city_fetch_by_state.py` — Prints city-state pairs using ORM relationships.
- `100-relationship_states_cities.sql` — SQL setup for one-to-many relationship schema.
- `100-relationship_states_cities.py` / `relationship_state.py` / `relationship_city.py` — ORM models and relationship setup for states/cities.
- `101-relationship_states_cities.sql` — SQL support for relationship list task.
- `101-relationship_states_cities_list.py` — Lists states with child city objects.
- `102-relationship_cities_states_list.py` — Lists each city with its parent state.
- `model_city.py` — SQLAlchemy city model used in ORM tasks.
