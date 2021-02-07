import sys
sys.path.append('.')
import pytest
from models.product_model import Product


class TestModel:
    @pytest.mark.parametrize('name, price, description',
                             [('Nome01', 1.1, 'Desc001'),
                              ('Nome01', 1.1, None)
                              ])
    def test_product_instance(self, name, price, description):
        product = Product(name, price, description)
        assert isinstance(product, Product)
        assert product.name == name
        assert product.price == price
        assert product.description == description

    def test_name_is_empty(self):
        with pytest.raises(ValueError):
            product = Product('', 1.1, 'Desc')

    def test_name_is_bigger_than_hundred(self):
        with pytest.raises(ValueError):
            product = Product('N' * 101, 2.1)

    def test_name_is_not_str(self):
        with pytest.raises(TypeError):
            product = Product(7, 1.5)

    def test_description_is_bigger_than_255(self):
        with pytest.raises(ValueError):
            product = Product('N', 2.1, 'D' * 256)

    def test_description_is_not_str(self):
        with pytest.raises(TypeError):
            product = Product('N', 1.5, 1)

    def test_price_is_not_float(self):
        with pytest.raises(TypeError):
            product = Product('N', '', 'd')
