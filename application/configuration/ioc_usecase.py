from dependency_injector import containers, providers

from application.configuration.ioc_providers import IOCProviders
from application.core.factory.account_factory import AccountFactory
from application.core.usecase.create_new_account_use_case import CreateNewAccountUseCase


class IOCUsecase(containers.DeclarativeContainer):
    """IoC container of usecase providers."""

    create_new_account_use_case = providers.Factory(
        CreateNewAccountUseCase,
        validator=IOCProviders.account_validator_provider,
        encryptor=IOCProviders.password_security_provider,
        factory=providers.Factory(AccountFactory),
        repository=IOCProviders.account_database_data_provider()
    )
