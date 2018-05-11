from application.configuration.ioc_usecase import IOCUseCase
from application.core.usecase.usecase_input import UseCaseInput
from application.core.usecase.usecase_output import UseCaseStatusEnum, UseCaseMessageEnum
from tests.base_tests import E2ETest


class TestRegisterAccountHappyPath(E2ETest):
    def test_succesfully_register_new_account(self):
        # Given
        usecase = IOCUseCase.register_account_use_case()
        usecase_input = UseCaseInput(payload={
            'username': 'Bertrand',
            'email': 'bertrand@test.com',
            'password': 'Password01!'
        })

        # When
        usecase_output = usecase.handle(usecase_input)

        # Then
        assert usecase_output.status == UseCaseStatusEnum.success
        assert usecase_output.message == UseCaseMessageEnum.account_registered
        assert usecase_output.content['account_id'] == 1
        assert usecase_output.content['activation_token']
