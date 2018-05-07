import abc


class ValidateAccountPayloadPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def validate_payload(self, payload: dict):
        raise NotImplementedError('users must define validate_payload to use this base class')
