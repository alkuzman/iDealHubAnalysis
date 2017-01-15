from flask import Flask
from app.rest_methods import rest
from app.test import test

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(rest)
app.run()
app.register_blueprint(test)