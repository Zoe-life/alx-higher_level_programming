from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # Define the base class for all models


class State(Base):
    """
    Representation of a state in the database.
    """
    __tablename__ = 'states'  # Table name in the database

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


def main():
    """
    Connects to the MySQL database and creates the 'states' table if it doesn't exist.
    """
    from sqlalchemy import create_engine

    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <username> <password> <database_name>")
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

    # Create all tables in the database (if they don't exist already)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()