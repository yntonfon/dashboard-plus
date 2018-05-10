from enum import Enum


class UsecaseStatusEnum(Enum):
    success = 'SUCCESS'
    failure = 'FAILURE'


class UsecaseMessageEnum(Enum):
    account_not_registered = 'Account registering failed'
    account_registered = 'Account registered with success'


class UsecaseDescriptionEnum(Enum):
    invalid_input_data = 'Invalid input data'
    account_already_exists = 'Account already exists'
    unexpected_error = 'An unexpected error occured, please try later'


class UsecaseOutput:
    def __init__(self, status=None, message=None, description=None, content=None):
        self.status = status
        self.message = message
        self.description = description
        self.content = content
