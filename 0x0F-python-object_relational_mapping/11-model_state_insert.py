from model_state import Base, State
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, creates a new "Louisiana" state object, adds it to the database, and prints its ID.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./model_state_insert.py <username> <password> <database_name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}', pool_pre_ping=True
    )

    # Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit changes to the database
    session.commit()

    # Query for the newly added state
    query = select(State).filter(State.name == "Louisiana")
    state = session.execute(query.first())

    # Print the state ID
    print(state.id)


if __name__ == "__main__":
    main()