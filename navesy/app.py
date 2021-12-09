from flask import Flask
from flask_admin import Admin

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
admin = Admin(app)


