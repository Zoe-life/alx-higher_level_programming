from relationship_state import State
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, retrieves all State objects with their Cities, and prints them.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <username> <password> <database_name>")
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

    # Single query to join State and City, order by state.id and city.id
    query = select(State, City).join(City).order_by(State.id, City.id)

    # Loop through results and print state and city information
    for state, city in query.all():
        print(f"{state.id}: {state.name}")
        print(f"\t{city.id}: {city.name}")


if __name__ == "__main__":
    main()