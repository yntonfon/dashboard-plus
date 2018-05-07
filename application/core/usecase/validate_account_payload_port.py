import abc


class ValidateAccountCreationtPayloadPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def validate_creation_payload(self, payload):
        raise NotImplementedError('users must define validate_creation_payload to use this base class')
