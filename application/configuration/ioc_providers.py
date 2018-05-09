import bcrypt
from dependency_injector import containers, providers

from application.configuration import config
from application.providers.security import PasswordSecurityProvider
from application.providers.validator import AccountValidatorProvider
from application.providers.validator.account_schema import AccountSchema


class IOCProviders(containers.DeclarativeContainer):
    """IoC container of providers."""

    password_security_provider = providers.Singleton(PasswordSecurityProvider, crypto=bcrypt, config=config)

    account_schema = providers.Singleton(AccountSchema)
    account_validator_provider = providers.Singleton(AccountValidatorProvider, schema=account_schema)
