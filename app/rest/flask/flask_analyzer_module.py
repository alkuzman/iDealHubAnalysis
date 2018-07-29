from dependency_injector import containers, providers

from app.rest.flask.analyzer_methods import rest


class FlaskAnalyzerModule(containers.DeclarativeContainer):
    analyzer_blueprint = providers.Object(rest)
