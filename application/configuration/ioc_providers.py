import bcrypt
from dependency_injector import containers, providers

from application.configuration import config
from application.providers.security import PasswordSecurityProvider


class IOCProviders(containers.DeclarativeContainer):
    """IoC container of providers."""

    password_security_provider = providers.Singleton(PasswordSecurityProvider, crypto=bcrypt, config=config)
