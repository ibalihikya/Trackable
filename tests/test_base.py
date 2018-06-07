from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from tests.file_util import*
import unittest
import json
import psycopg2
import json
from pprint import pprint



class SignUpTest(unittest.TestCase):
         
    def setUp(self):
        """create new tables in the database before each test.""" 
        try:
            self.connection = psycopg2.connect(
                "dbname='trackable_db' user='postgres' host='localhost' password='Dreamalive1' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        
        except:
            return "Cannot connect to database"
              
        create_user_requests_table_command = "CREATE TABLE user_requests(id serial PRIMARY KEY, title varchar(100), description varchar (100),\
                                   status integer NOT NULL, userid integer NOT NULL)"
        self.cursor.execute(create_user_requests_table_command)

        create_users_table_command = "CREATE TABLE users(id serial PRIMARY KEY, username varchar(100), public_id varchar(100), password varchar(100),\
                                    admin boolean NOT NULL)"
        self.cursor.execute(create_users_table_command)


    def tearDown(self):
        """Drop tables after each test."""
        try:
            self.connection = psycopg2.connect(
            "dbname='trackable_db' user='postgres' host='localhost' password='Dreamalive1' port='5432'")

            drop_user_requests_table_command = "DROP TABLE user_requests"
            self.cursor.execute(drop_user_requests_table_command)
    
            drop_users_table_command = "DROP TABLE users"
            self.cursor.execute(drop_users_table_command)


        except:
            return "Can not connect to database or drop tables"
   
    


    def test_database(self):
        """Check that the database exists"""
        connected = False
        try:
            self.connection = psycopg2.connect(
            "dbname='trackable_db' user='postgres' host='localhost' password='Dreamalive1' port='5432'")
            connected = True
        except:
            connected = False

        self.assertTrue(connected)

    def test_signup_valid_input(self):
        """ Test user sign up with valid inputs"""
        testobj = app.test_client(self)
        response = testobj.post('/api/v1/auth/signup', json=new_user1_data )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), new_user_creation_success)

    


    











   
     
