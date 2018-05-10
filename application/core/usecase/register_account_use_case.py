from application.core.usecase.base_usecase import BaseUsecase
from application.core.usecase.usecase_input import UsecaseInput
from application.core.usecase.usecase_output import UsecaseOutput


class RegisterAccountUseCase(BaseUsecase):
    def __init__(self, create_account_step):
        self.create_account_step = create_account_step

    def handle(self, usecase_input: UsecaseInput) -> UsecaseOutput:
        pass
