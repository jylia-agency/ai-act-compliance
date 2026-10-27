"""Modèles de données (ORM SQLAlchemy). « Model » désigne ici une table, pas un modèle d'IA."""
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    model_number = Column(String(32))  # référence d'édition


class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    reader_id = Column(Integer)
    start = Column(Date)
