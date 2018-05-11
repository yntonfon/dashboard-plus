from application.core.exception.dashboardplus_exception import PersitenceException
from application.core.port.decode_safe_time_token_port import DecodeActivationAccountTokenPort
from application.core.port.does_account_exist_port import DoesAccountExistPort
from application.core.port.update_email_confirmed_port import UpdateEmailConfirmedPort
from application.core.usecase.base_usecase import BaseUseCase
from application.core.usecase.usecase_input import UseCaseInput
from application.core.usecase.usecase_output import (
    UseCaseOutput, UsecaseStatusEnum, UseCaseMessageEnum,
    UseCaseDescriptionEnum
)


class ActivateAccountUseCase(BaseUseCase):
    def __init__(self, decode_token_provider: DecodeActivationAccountTokenPort,
                 does_account_exist_provider: DoesAccountExistPort,
                 update_email_confirmed_provider: UpdateEmailConfirmedPort):
        self.update_email_confirmed_provider = update_email_confirmed_provider
        self.does_account_exist_provider = does_account_exist_provider
        self.decode_token_provider = decode_token_provider

    def handle(self, usecase_input: UseCaseInput) -> UseCaseOutput:
        usecase_output = UseCaseOutput()

        email = self._get_email_from_token(usecase_input.payload)
        if email:
            self._udpate_email_confirmed(email, usecase_output)
        else:
            self._set_token_failure(usecase_output)

        return usecase_output

    def _get_email_from_token(self, token):
        return self.decode_token_provider.decode_activation_account_token(token)

    def _udpate_email_confirmed(self, email, usecase_output):
        try:
            if self.does_account_exist_provider.does_account_exist(email):
                self.update_email_confirmed_provider.update_email_confirmed(email, True)
                self._set_success_output(usecase_output)
            else:
                self._set_account_not_found_failure(usecase_output)
        except PersitenceException:
            self._set_persistence_failure(usecase_output)

    def _set_account_not_found_failure(self, usecase_output):
        self._set_failure_status_and_message(usecase_output)
        usecase_output.description = UseCaseDescriptionEnum.account_does_not_exist

    def _set_token_failure(self, usecase_output):
        self._set_failure_status_and_message(usecase_output)
        usecase_output.description = UseCaseDescriptionEnum.invalid_token

    def _set_persistence_failure(self, usecase_output):
        self._set_failure_status_and_message(usecase_output)
        usecase_output.description = UseCaseDescriptionEnum.unexpected_error

    @staticmethod
    def _set_failure_status_and_message(usecase_output):
        usecase_output.status = UsecaseStatusEnum.failure
        usecase_output.message = UseCaseMessageEnum.account_not_activated

    @staticmethod
    def _set_success_output(usecase_output):
        usecase_output.status = UsecaseStatusEnum.success
        usecase_output.message = UseCaseMessageEnum.account_activated
