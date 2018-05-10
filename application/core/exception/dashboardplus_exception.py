import abc


class DashboardPlusException(Exception, metaclass=abc.ABCMeta):
    def __init__(self):
        raise NotImplementedError('users must inherate to use this base class')


class OutputException(DashboardPlusException):
    def __init__(self, messages=None):
        self.messages = messages


class InputValidationException(OutputException):
    pass


class AppDataDuplicationException(OutputException):
    pass


class AppUnexpectedFailureException(OutputException):
    pass


class InputException(DashboardPlusException):
    def __init__(self, messages=None, origins=None):
        self.origins = origins
        self.messages = messages


class EntityAlreadyExistsException(InputException):
    def __init__(self, name: str, keys: tuple):
        self.messages = 'An entity {0} is already created with fields {1}'.format(name, repr(keys))


class PersitenceException(InputException):
    pass
