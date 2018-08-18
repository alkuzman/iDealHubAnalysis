import os

from dependency_injector import containers, providers

SSL_CERTIFICATE_ENV = 'APP_SSL_CERTIFICATE'
SSL_PRIVATE_KEY_ENV = 'APP_SSL_PRIVATE_KEY'
APPLICATION_NAME_ENV = 'APP_NAME'


class EnvModule(containers.DeclarativeContainer):
    ssl_certificate = providers.Object(os.environ.get(SSL_CERTIFICATE_ENV))
    ssl_private_key = providers.Object(os.environ.get(SSL_PRIVATE_KEY_ENV))
    application_name = providers.Object(os.environ.get(APPLICATION_NAME_ENV) or "KluppsAnalyzer")
