from model_state import Base, State
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, updates the state with ID 2 to "New Mexico", and confirms the update.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./model_state_update_id_2.py <username> <password> <database_name>")
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

    # Query for the state with ID 2
    query = select(State).filter(State.id == 2)
    state = session.execute(query.first())

    if state:  # Update the state if it exists
        state.name = "New Mexico"
        session.commit()
        print("State updated")
    else:
        print("State not found")


if __name__ == "__main__":
    main()