import abc


class UpdateEmailConfirmedPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update_email_confirmed(self, email: str, value: bool) -> None:
        raise NotImplementedError('users must define update_email_confirmed to use this base class')
