from flask import Flask
from app.rest_methods import rest
from app.test import test

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(rest)
app.run(ssl_context=(
    "./ssl/idealclient.com.crt",
    "./ssl/idealclient.com.key"))
app.register_blueprint(test)
