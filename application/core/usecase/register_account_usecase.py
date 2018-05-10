from application.core.exception.dashboardplus_exception import (
    InputValidationException, UnexpectedFailureException,
    AccountAlreadyExistsException
)
from application.core.usecase.base_usecase import BaseUseCase
from application.core.usecase.steps import CreateAccountStep, CreateAccountActivationTokenStep
from application.core.usecase.usecase_input import UseCaseInput
from application.core.usecase.usecase_output import (
    UseCaseOutput, UsecaseStatusEnum, UseCaseMessageEnum,
    UseCaseDescriptionEnum
)


class RegisterAccountUseCase(BaseUseCase):
    def __init__(self, create_account_step: CreateAccountStep, create_token_step: CreateAccountActivationTokenStep):
        self.create_token_step = create_token_step
        self.create_account_step = create_account_step

    def handle(self, usecase_input: UseCaseInput) -> UseCaseOutput:
        usecase_output = UseCaseOutput()

        try:
            account_id = self.create_account_step.execute(usecase_input.payload)
            token = self.create_token_step.execute(usecase_input.payload['email'])
        except InputValidationException as error:
            self.set_status_and_message_error(usecase_output)
            usecase_output.description = UseCaseDescriptionEnum.invalid_input_data
            usecase_output.content = error.messages
        except AccountAlreadyExistsException:
            self.set_status_and_message_error(usecase_output)
            usecase_output.description = UseCaseDescriptionEnum.account_already_exists
        except UnexpectedFailureException:
            self.set_status_and_message_error(usecase_output)
            usecase_output.description = UseCaseDescriptionEnum.unexpected_error
        else:
            usecase_output.status = UsecaseStatusEnum.success
            usecase_output.message = UseCaseMessageEnum.account_registered
            usecase_output.content = {
                'account_id': account_id,
                'activation_token': token
            }

        return usecase_output

    @staticmethod
    def set_status_and_message_error(usecase_output):
        usecase_output.status = UsecaseStatusEnum.failure
        usecase_output.message = UseCaseMessageEnum.account_not_registered
