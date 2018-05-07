import abc

from application.core.entity.account import Account


class InsertAccountPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(self, account: Account):
        raise NotImplementedError('users must define insert to use this base class')
