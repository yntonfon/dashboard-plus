from dependency_injector import containers, providers

from application.configuration.ioc_providers import IOCProviders
from application.core.factory.account_factory import AccountFactory
from application.core.usecase.steps.create_account_step import CreateAccountStep


class IOCUsecaseSteps(containers.DeclarativeContainer):
    """IoC container of usecase providers."""

    create_account_step = providers.Factory(
        CreateAccountStep,
        validator=IOCProviders.account_validator_provider,
        encryptor=IOCProviders.password_security_provider,
        factory=providers.Factory(AccountFactory),
        repository=IOCProviders.account_database_data_provider()
    )
