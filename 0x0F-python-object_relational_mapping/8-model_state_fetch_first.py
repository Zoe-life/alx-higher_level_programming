from model_state import Base, State
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, retrieves the first State object, and prints it or "Nothing" if none exists.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./model_state_fetch_first.py <username> <password> <database_name>")
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

    # Query for the first State object (order by id)
    query = select(State).order_by(State.id).limit(1)
    first_state = session.execute(query).scalars().first()

    # Print the state details or "Nothing" if no state was found
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()