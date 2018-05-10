import abc


class BaseStep(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, payload):
        raise NotImplementedError('users must define execute to use this base class')
