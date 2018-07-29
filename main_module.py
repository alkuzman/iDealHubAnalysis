from dependency_injector import containers, providers

from application import Application


class MainModule(containers.DeclarativeContainer):
    application_provider = providers.Singleton(Application)
