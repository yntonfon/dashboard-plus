from application.core.entity.account import Account


class AccountFactory:

    @staticmethod
    def create(payload: dict) -> Account:
        return Account(**payload)
