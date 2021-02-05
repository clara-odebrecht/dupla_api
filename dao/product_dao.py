import sys
sys.path.append('.')
from model.product_model import Product
from dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)


dao = ProductDao()

product_model = Product('Name1', 111., 'Des01')
dao.save(product_model)
product = dao.read_all()
for p in product:
    print(p.name)
