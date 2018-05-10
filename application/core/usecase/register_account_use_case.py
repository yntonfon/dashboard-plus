from application.core.exception.dashboardplus_exception import (
    InputValidationException, UnexpectedFailureException,
    AccountAlreadyExistsException
)
from application.core.usecase.base_usecase import BaseUsecase
from application.core.usecase.steps import CreateAccountStep
from application.core.usecase.usecase_input import UsecaseInput
from application.core.usecase.usecase_output import UsecaseOutput, UsecaseStatusEnum, UsecaseMessageEnum


class RegisterAccountUseCase(BaseUsecase):
    def __init__(self, create_account_step: CreateAccountStep):
        self.create_account_step = create_account_step

    def handle(self, usecase_input: UsecaseInput) -> UsecaseOutput:
        usecase_output = UsecaseOutput()

        try:
            result = self.create_account_step.execute(usecase_input.payload)
        except InputValidationException as error:
            usecase_output.status = UsecaseStatusEnum.failure
            usecase_output.message = UsecaseMessageEnum.invalid_input_data
            usecase_output.description = error.messages
        except AccountAlreadyExistsException:
            usecase_output.status = UsecaseStatusEnum.failure
            usecase_output.message = UsecaseMessageEnum.account_already_exists
        except UnexpectedFailureException:
            usecase_output.status = UsecaseStatusEnum.failure
            usecase_output.message = UsecaseMessageEnum.unexpected_error
        else:
            usecase_output.status = UsecaseStatusEnum.success
            usecase_output.message = UsecaseMessageEnum.account_created
            usecase_output.content = result

        finally:
            return usecase_output
