from flask import Flask, request, Blueprint, jsonify
from flask_restplus import Namespace, Resource, fields, Api
from app.customer.models  import Customer

app = Flask(__name__)

api = Namespace('customer', description='customer related operations')

@api.route('/')
class CustomerDetails(Resource):
    def post(self):
        # if request.method=='POST':
        raw_data = request.get_json(force=True)
        if "name" in raw_data:
            name = raw_data.get("name")
        if "email" in raw_data:
            email = raw_data.get("email")
        if "address" in raw_data:
            address = raw_data.get("address")
        customer = Customer.auery.filter_by(email=email)
        if not customer:
            new_customer = Customer(name=name, email=email, address=address)
            db.session.add(new_customer)
            db.session.commit()
        return 'successfull', 200

api.add_resource(CustomerDetails, '/')
