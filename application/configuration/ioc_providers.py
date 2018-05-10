import bcrypt
from dependency_injector import containers, providers
from itsdangerous import URLSafeTimedSerializer

from application.configuration import config
from application.configuration.ioc_database import IOCDatabase
from application.providers.data.account_database_data_provider import AccountDatabaseDataProvider
from application.providers.security import PasswordSecurityProvider
from application.providers.security.token_security_provider import TokenSecurityProvider
from application.providers.validator import AccountValidatorProvider
from application.providers.validator.account_schema import AccountSchema


class IOCProviders(containers.DeclarativeContainer):
    """IoC container of providers."""

    password_security_provider = providers.Singleton(
        PasswordSecurityProvider,
        crypto=bcrypt,
        config=config
    )

    account_validator_provider = providers.Singleton(
        AccountValidatorProvider,
        schema=providers.Factory(AccountSchema)
    )

    account_database_data_provider = providers.Singleton(
        AccountDatabaseDataProvider,
        db=IOCDatabase.db
    )

    token_security_provider = providers.Singleton(
        TokenSecurityProvider,
        crypto=providers.Factory(URLSafeTimedSerializer, config.SECRET_KEY),
        config=config
    )
