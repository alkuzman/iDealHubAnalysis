import string

from flask import Flask

from app.rest.flask.analyzer_methods import rest
from application import Application


class FlaskApplication(Application):
    def __init__(self, flask: Flask, ssl_certificate_path: string, ssl_private_key_path: string, **kwargs):
        super().__init__()
        self.flask = flask
        self.ssl_certificate_path = ssl_certificate_path
        self.ssl_private_key_path = ssl_private_key_path
        self.blueprints = kwargs

    def run(self):
        for blueprint in self.blueprints:
            self.flask.register_blueprint(self.blueprints[blueprint])
        if self.ssl_certificate_path is not None and self.ssl_private_key_path is not None:
            self.flask.run(
                ssl_context=(
                    self.ssl_certificate_path,
                    self.ssl_private_key_path
                )
            )
        else:
            self.flask.run()
