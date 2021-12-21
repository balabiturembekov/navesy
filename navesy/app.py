from flask import Flask
from flask_admin import Admin

from settings import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
admin = Admin(app)


