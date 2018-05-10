import abc

from application.core.usecase.usecase_input import UseCaseInput
from application.core.usecase.usecase_output import UseCaseOutput


class BaseUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, usecase_input: UseCaseInput) -> UseCaseOutput:
        raise NotImplementedError('users must define handle to use this base class')
