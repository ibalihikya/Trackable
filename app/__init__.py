# Import flask and template operators
from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Configurations
#app.config.from_object('config')

# Import a module / component using its blueprint handler variable (mod_auth)
from app.views.users_view import mod_auth

# Register blueprint(s)
app.register_blueprint(mod_auth)


