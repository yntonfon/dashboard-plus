import abc


class DoesAccountExistPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def does_account_exist(self, email: str) -> bool:
        raise NotImplementedError('users must define does_account_exist to use this base class')
