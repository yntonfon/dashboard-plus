from application.configuration.ioc_usecase import IOCUseCase
from application.core.usecase.usecase_input import UseCaseInput
from application.core.usecase.usecase_output import UseCaseStatusEnum, UseCaseMessageEnum
from tests.base_tests import E2ETest


class TestActivateAccountHappyPath(E2ETest):
    def test_succesfully_activate_new_account(self):
        # Given
        usecase = IOCUseCase.activate_account_use_case()
        token = self._given_a_registered_account()
        usecase_input = UseCaseInput(payload=token)

        # When
        usecase_output = usecase.handle(usecase_input)

        # Then
        assert usecase_output.status == UseCaseStatusEnum.success
        assert usecase_output.message == UseCaseMessageEnum.account_activated

    @staticmethod
    def _given_a_registered_account():
        usecase = IOCUseCase.register_account_use_case()
        usecase_input = UseCaseInput(payload={
            'username': 'Bertrand',
            'email': 'bertrand@test.com',
            'password': 'Password01!'
        })
        result = usecase.handle(usecase_input)
        return result.content['activation_token']
