import abc

from application.core.entity.account import Account


class CreateAccountPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_account(self, payload: dict) -> Account:
        raise NotImplementedError('users must define create_account to use this base class')
