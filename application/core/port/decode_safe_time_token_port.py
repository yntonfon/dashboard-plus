import abc


class DecodeActivationAccountTokenPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def decode_activation_account_token(self, token: str) -> object:
        raise NotImplementedError('users must define decode_activation_account_token to use this base class')
