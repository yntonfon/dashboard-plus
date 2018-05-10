from enum import Enum


class UsecaseStatusEnum(Enum):
    success = 'SUCCESS'
    failure = 'FAILURE'


class UseCaseMessageEnum(Enum):
    account_not_registered = 'Account registering failed'
    account_registered = 'Account registered with success'
    account_activated = 'Account activated with success'
    account_not_activated = 'Account not activated'


class UseCaseDescriptionEnum(Enum):
    invalid_input_data = 'Invalid input data'
    account_already_exists = 'Account already exists'
    unexpected_error = 'An unexpected error occured, please try later'
    invalid_token = 'Token is invalid'
    account_does_not_exist = 'Account does not exist'


class UseCaseOutput:
    def __init__(self, status=None, message=None, description=None, content=None):
        self.status = status
        self.message = message
        self.description = description
        self.content = content
