from model_state import Base, State
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, retrieves all State objects, and prints them in ascending order by id.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./model_state_fetch_all.py <username> <password> <database_name>")
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

    # Query all State objects sorted by id
    query = select(State).order_by(State.id)
    states = session.execute(query).scalars().all()

    # Print each state's id and name
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()