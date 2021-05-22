from flask import Flask
from  .config import DATABASE_URI
from  app.customer.models import db
from flask_restplus import Api

def create_app():
    app = Flask(__name__)

    db.init_app(app)
    from app.api_v1.customer import api as customer_api


    api.add_namespace(customer_api)