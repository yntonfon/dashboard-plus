from application.core.entity.account import Account
from application.core.port.create_account_port import CreateAccountPort


class AccountFactory(CreateAccountPort):

    def create_account(self, payload: dict) -> Account:
        return Account(**payload)
