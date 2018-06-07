import psycopg2
from app.models import User
from pprint import pprint

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='trackable_db' user='postgres' host='localhost' password='Dreamalive1' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        
        except:
            pprint("Cannot connect to database")

      
    
    def insert_user(self, user):
        insert_user_command = "INSERT INTO users(username, public_id, password, admin) VALUES('" + user.username  + "','" + user.public_id +  "','" + user.password + "','" + user.admin + "')"
        self.cursor.execute(insert_user_command)

    

#if __name__== '__main__':
    #database_connection = DatabaseConnection()
    # database_connection.create_table()
    # database_connection.insert_new_record()
    # database_connection.query_all()
    # database_connection.update_record()
    #database_connection.drop_table()
