from application.configuration.ioc_usecase import IOCUsecase
from application.providers.data.account_data_mapper import AccountMapper
from tests.base_tests import E2ETest


class TestCreateAccountHappyPath(E2ETest):
    def test_succesfully_create_a_new_account(self):
        # Given
        input_payload = {
            'username': 'Bertrand',
            'email': 'bertrand@test.com',
            'password': 'Password01!'
        }
        use_case = IOCUsecase.create_new_account_use_case()

        # When
        use_case.execute(input_payload)

        # Then
        account = self.db.session.query(AccountMapper).first()
        assert 1 == account.id
        assert 'Bertrand' == account.username
