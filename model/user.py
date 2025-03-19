
import uuid

from sqlalchemy import VARCHAR, Column, LargeBinary, String

from model.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(VARCHAR(100))
    email = Column(String, unique=True)
    password = Column(LargeBinary)
