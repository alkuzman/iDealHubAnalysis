import os

from dependency_injector import containers, providers
from flask import Flask

from app.rest.flask.flask_analyzer_module import FlaskAnalyzerModule
from env_module import EnvModule
from flask_application import FlaskApplication
from main_module import MainModule


@containers.override(MainModule)
class FlaskMainModule(containers.DeclarativeContainer):
    flask_instance_relative_config = providers.Object(True)

    flask_provider = providers.Singleton(Flask,
                                         import_name=EnvModule.application_name,
                                         instance_relative_config=flask_instance_relative_config)

    application_provider = providers.Singleton(FlaskApplication,
                                               flask=flask_provider,
                                               ssl_certificate_path=EnvModule.ssl_certificate,
                                               ssl_private_key_path=EnvModule.ssl_private_key,
                                               analyzer_blueprint=FlaskAnalyzerModule.analyzer_blueprint)
