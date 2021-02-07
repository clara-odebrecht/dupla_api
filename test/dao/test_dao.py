import sys

sys.path.append('.')

import pytest
from models.product_model import Product
from dao.product_dao import ProductDao


class TestDao:
    @pytest.fixture
    def create_instance(self):
        product = Product('name', 1.1, 'des')
        return product

    def test_instance(self):
        prod_dao = ProductDao()
        assert isinstance(prod_dao, ProductDao)

    def test_create(self, create_instance):
        product = create_instance
        prod_dao = ProductDao()
        new_prod = prod_dao.save(product)
        assert new_prod is not None
        assert new_prod.name == product.name
        assert new_prod.price == product.price
        assert new_prod.description == product.description
        prod_dao.delete(new_prod)

    def test_read_by_id(self, create_instance):
        product = create_instance
        prod_dao = ProductDao()
        new_prod = prod_dao.save(product)
        result = prod_dao.read_by_id(new_prod.id)
        assert isinstance(result, Product)
        assert new_prod.name == result.name
        assert new_prod.price == result.price
        assert new_prod.description == result.description
        prod_dao.delete(new_prod)

    def test_read_all(self):
        result = ProductDao().read_all()
        assert isinstance(result, list)

    def test_delete(self, create_instance):
        prod_dao = ProductDao()
        new_prod = prod_dao.save(create_instance)
        result = prod_dao.read_by_id(new_prod.id)
        prod_dao.delete(result)
        result = prod_dao.read_by_id(new_prod.id)
        assert result is None
