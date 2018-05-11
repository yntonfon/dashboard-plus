import abc


class CreateAccountActivationTokenPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_account_activation_token(self, payload):
        raise NotImplementedError('users must define create_account_activation_token to use this base class')
