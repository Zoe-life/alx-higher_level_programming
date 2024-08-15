from model_state import Base, State
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, retrieves the State object with the provided name, and prints its ID or "Not found" if not found.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 5:
        print("Usage: ./model_state_my_get.py <username> <password> <database_name> <state_name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}', pool_pre_ping=True
    )

    # Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()

    # Filter states with the provided name (parameterized query)
    query = select(State).filter(State.name == state_name)
    state = session.execute(query.params(state_name=state_name)).first()

    # Print the state ID or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()