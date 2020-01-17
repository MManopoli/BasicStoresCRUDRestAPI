from flask_restful import Resource, reqparse
from models.user import UserModel


# "Resources" are the external representation of some thing
# Also, because we're using Flask-RESTful, these objects are extending flask_restful.Resource
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help="This field cannot be left blank."
    )
    parser.add_argument(
        'password', type=str, required=True, help="This field cannot be left blank."
    )

    def post(self):
        request_data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(request_data['username']):
            return {"message": f"A user with username '{request_data['username']}' already exists."}, 400  # BAD REQUEST

        user = UserModel(**request_data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201  # 201 == CREATED
