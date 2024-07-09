from .database import Base
from sqlalchemy import Column, Integer, String


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    cooking_time = Column(Integer, index=True)
    ingredients = Column(String, index=True)
    views = Column(Integer, index=True, default=0)
