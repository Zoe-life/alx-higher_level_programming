from sqlalchemy import Column, Integer, String, ForeignKey, relationship
from sqlalchemy.orm import backref


class State(Base):
    """
    State class representing a state in a country.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    # Relationship with the City class (one-to-many)
    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan", passive_deletes=True
    )

    def __repr__(self):
        """
        String representation of a State object.
        """
        return f"<State id={self.id}> {self.name}"