import abc


class DashboardPlusException(Exception, metaclass=abc.ABCMeta):
    def __init__(self):
        raise NotImplementedError('users must inherate to use this base class')


class InnerAppException(DashboardPlusException):
    def __init__(self, messages=None):
        self.messages = messages


class InputValidationException(InnerAppException):
    pass


class AccountAlreadyExistsException(InnerAppException):
    pass


class UnexpectedFailureException(InnerAppException):
    pass


class ProviderInputException(DashboardPlusException):
    def __init__(self, messages=None, origins=None):
        self.origins = origins
        self.messages = messages


class EntityAlreadyExistsException(ProviderInputException):
    def __init__(self, name: str, keys: tuple):
        self.messages = 'An entity {0} is already created with fields {1}'.format(name, repr(keys))


class PersitenceException(ProviderInputException):
    pass
