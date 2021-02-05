from flask import Flask
from flask_restful import Api, fields
from controller.product_resource import ProductResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/api/product', endpoint='products')
api.add_resource(ProductResource, '/api/product/<int:id>', endpoint='product')

app.run(debug=True)
