#from flask import Flask
from app import create_app
#from app.api_v1.customer import api

#app = Flask(__name__)
app = create_app()

#api = Api(app)
#api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)