from enum import Enum


class UsecaseStatusEnum(Enum):
    success = 'SUCCESS'
    failure = 'FAILURE'


class UsecaseMessageEnum(Enum):
    invalid_data = 'Invalid data'
    account_already_exist = 'Account already exists'
    unexpected_error = 'An unexpected error occured, please try later'


class UsecaseOutput:
    def __init__(self, status=None, message=None, description=None, content=None):
        self.status = status
        self.message = message
        self.description = description
        self.content = content
