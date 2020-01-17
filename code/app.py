from datetime import timedelta

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.store import Store, StoreList
from resources.item import Item, ItemList
import os

app = Flask(__name__)
# application SQLAlchemy configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///./data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Tracks every change to session unless we set this to False
app.secret_key = 'SuperSecretKeyThing'
api = Api(app)

# application JWT configurations
app.config['JWT_AUTH_URL_RULE'] = '/login'  # Change authentication endpoint to login instead of /auth
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)  # Config JWT to expire within half an hour
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'  # Config JWT auth key name to be 'email' instead of default 'username'
jwt = JWT(app, authenticate, identity)  # creates /auth endpoint

# Sometimes we may want to include more information in the authentication response body, such as the user's ID:
@ jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify(
        {
            'access_token': access_token.decode('utf-8'),
            'user_id': identity.id
        }
    )


# By default, Flask-JWT raises JWTError when an error occurs.
# We can customize what our flask app does when this happens:
@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify(
        {
            'message': error.description,
            'code': error.status_code,
        }
    ), error.status_code


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
