from flask_restful import Resource, reqparse
from flask import jsonify
from ..extensions import db
from ..models.user import User
from flask_jwt_extended import create_access_token

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('password', type=str, required=True, help='Password is required')

class AuthRegisterAPI(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

class AuthLoginAPI(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token}
