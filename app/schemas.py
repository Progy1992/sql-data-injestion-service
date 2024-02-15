from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "book"

    isbn = Column(String(255), primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    publicationYear = Column(Integer, nullable=False)
    publisher = Column(String(255), nullable=False)
    image = Column(String(500))
    is_active = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False, onupdate=datetime.utcnow())


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    isbn = Column(String(500), nullable=False)
    rating = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False, onupdate=datetime.utcnow())


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    age = Column(Integer)
    is_active = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False, onupdate=datetime.utcnow)
