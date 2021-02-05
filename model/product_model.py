import sys
sys.path.append('.')
from utils.validators import validate_type, validate_not_empty, validate_length
from sqlalchemy import Column, String, Float
from model.base_model import BaseModel
from sqlalchemy.orm import validates


class Product(BaseModel):
    __tablename__ = 'PRODUCT'
    name = Column('name', String(length = 100), nullable = False)
    price = Column('price', Float, nullable = False)
    description = Column('description', String(length = 255), nullable = True)

    def __init__(self, name: str, price: float, description: str = None) -> None:
        self.name = name
        self.price = price
        self.description = description

    @validates('name')
    def validate_name(self, key, name) -> None:
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        return validate_length(name, 100, key)

    @validates('description')
    def validate_description(self, key, description) -> None:
        description = validate_type(description, str, key)
        return validate_length(description, 255, key)

    @validates('price')
    def validate_price(self, key, price) -> None:
        price = validate_type(price, float, key)
        return price
