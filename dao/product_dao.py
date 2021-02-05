import sys
sys.path.append('.')
from model.product_model import Product
from dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
