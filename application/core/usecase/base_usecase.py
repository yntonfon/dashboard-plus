import abc

from application.core.usecase.usecase_input import UsecaseInput
from application.core.usecase.usecase_output import UsecaseOutput


class BaseUsecase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, usecase_input: UsecaseInput) -> UsecaseOutput:
        raise NotImplementedError('users must define handle to use this base class')
