from sqlalchemy import Column, Integer, String
from database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    department = Column(String)
    position = Column(String)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
