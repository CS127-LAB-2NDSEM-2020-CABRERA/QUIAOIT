from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from db import connection, execute_query, execute_read_query
app = Flask(__name__)

import os
import json

# init app 
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Product Management API',
    description='A Product Management API',
)


basedir = os.path.abspath(os.path.dirname(__file__))





productRoutes = api.namespace('product-management/api', description='Product operations')


class ProductModel:
  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty


product = api.model('Product', {
    'id': fields.Integer(readonly=True, description='The Product unique identifier'),
    'name': fields.String(required=True, description='The name of the product'),
    'description': fields.String(required=True, description='The description of the product'),
    'price': fields.Float(required=True, description='The price of the product'),
    'qty': fields.Integer(required=True, description='the quantity of the product'),
})



@productRoutes.route('/products')
class ProductsList(Resource):
	def get(self):
		''' Get All Products'''
		all_products_query = "SELECT * from products"
		products = execute_read_query(all_products_query)
		productsList = []
		for product in products:
			print(products)
			productsList.append(vars(ProductModel(product[1],product[2],product[3],product[4])))
		return productsList, 200


@productRoutes.route('/product/<int:id>')
class Products(Resource):
	def get(self,id):
		''' Get a single product based on ID'''
		searchedID = str(id)
		infoToSearch = "SELECT * from products WHERE id="+searchedID
		result = execute_read_query(infoToSearch)
		if len(result) == 0:
			return "There is no recorded info on the given id number. It is possible that it is already deleted.", 200
		else:
			jsonResult = vars(ProductModel(result[0][1],result[0][2],result[0][3],result[0][4]))
			return jsonResult, 200

	def delete(self,id):
		''' Delete a single product based on ID'''
		idToDelete = str(id)
		infoToSearch = "SELECT * from products WHERE id="+idToDelete
		result = execute_read_query(infoToSearch)
		if len(result) == 0:
			return "Nothing to delete. Since, it is empty.", 304
		else:
			idToSearch = "DELETE FROM products WHERE id="+idToDelete
			execute_query(idToSearch)
			return "Product with id: "+str(id)+" is successfully deleted.", 200

	@productRoutes.expect(product)
	def put(self,id):
		''' Update a single product based on ID'''
		idToUpdate = str(id)
		infoToSearch = "SELECT * from products WHERE id="+idToUpdate
		result = execute_read_query(infoToSearch)
		if len(result) == 0:
			return "Cannot update", 304
		else:
			updatedInfo = [request.json.get('name'), request.json.get('description'), str(request.json.get('price')), str(request.json.get('qty'))]
			updateID = "UPDATE products SET name ='"+updatedInfo[0]+"', description ='"+updatedInfo[1]+"', price ="+updatedInfo[2]+", qty ="+updatedInfo[3]+" WHERE id="+idToUpdate
			execute_query(updateID)
			result = execute_read_query(infoToSearch)
			jsonResult = vars(ProductModel(result[0][1],result[0][2],result[0][3],result[0][4]))
			return "Product id: "+idToUpdate+" is updated. "+str(jsonResult), 200

# @productRoutes.route('/product')
# class Products(Resource):
# 	def post(self,)


# Run Server
if __name__ == '__main__':
	app.run(debug=True)