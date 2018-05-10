import abc


class CreateSafeTimedTokenPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_safe_time_token(self, payload):
        raise NotImplementedError('users must define create_safe_time_token to use this base class')
