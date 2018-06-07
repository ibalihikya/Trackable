from app import app
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from flask.views import MethodView
from werkzeug import check_password_hash, generate_password_hash
import psycopg2
from app.models import User
from app.db_calls import DatabaseConnection
import uuid

mod_auth = Blueprint('auth', __name__)
class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass

    def post(self):
        """"create a new user"""
        received_data = request.get_json()           
        validated = self.validate_user_input(received_data)
        if  not validated["status"]:
            response = jsonify({'message':validated['message']})
            response.status_code = 400
            return response
        hashed_password = generate_password_hash(received_data['password'], method='sha256')
        user = User()
        user.public_id = str(uuid.uuid4())
        user.username = received_data['username']
        user.password = hashed_password
        user.admin = "False"
    
        dbConnect = DatabaseConnection()
        dbConnect.insert_user(user)
        response = jsonify({'message':'signup successful!'})
        response.status_code = 201
        return response

        

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

    def validate_user_input(self, received_data):
        """validate user inputs"""
        #check username
        if  len(received_data['username']) == 0:
            return {'status': False, 'message':'missing username.'}
        elif len(received_data['password']) == 0: 
            return {'status': False, 'message':'missing password.'}    
        return {'status': True, 'message':'Data is valid.'}



user_view = UserAPI.as_view('user_api')

app.add_url_rule('/api/v1/auth/signup', view_func=user_view, methods=['POST',])
