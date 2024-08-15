from relationship_city import City
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, retrieves all City objects with their State names, and prints them.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <username> <password> <database_name>")
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

    # Single query to select City objects with state.name using the 'state' relationship
    query = select(City).join(City.state).order_by(City.id)

    # Loop through results and print city information with state name
    for city in query.all():
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    main()