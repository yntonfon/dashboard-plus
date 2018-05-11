from dependency_injector import containers, providers

from application.configuration.ioc_providers import IOCProviders
from application.core.factory.account_factory import AccountFactory
from application.core.usecase import RegisterAccountUseCase, ActivateAccountUseCase
from application.core.usecase.steps import CreateAccountActivationTokenStep
from application.core.usecase.steps.create_account_step import CreateAccountStep


class IOCUseCaseSteps(containers.DeclarativeContainer):
    """IoC container of use case step providers."""

    create_account_step = providers.Factory(
        CreateAccountStep,
        validator=IOCProviders.account_validator_provider,
        encryptor=IOCProviders.password_security_provider,
        factory=providers.Factory(AccountFactory),
        repository=IOCProviders.account_database_data_provider
    )

    create_account_activation_token_step = providers.Factory(
        CreateAccountActivationTokenStep,
        token_provider=IOCProviders.token_security_provider
    )


class IOCUseCase(containers.DeclarativeContainer):
    """IoC container of usecase providers."""

    register_account_use_case = providers.Factory(
        RegisterAccountUseCase,
        create_account_step=IOCUseCaseSteps.create_account_step,
        create_token_step=IOCUseCaseSteps.create_account_activation_token_step
    )

    activate_account_use_case = providers.Factory(
        ActivateAccountUseCase,
        decode_token_provider=IOCProviders.token_security_provider,
        does_account_exist_provider=IOCProviders.account_database_data_provider,
        update_email_confirmed_provider=IOCProviders.account_database_data_provider
    )
