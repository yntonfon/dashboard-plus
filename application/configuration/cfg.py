from os import environ

default_config = {
    'SECRET_KEY': environ.get('SECRET_KEY', 'secret_for_test'),
    'BCRYPT_DESIRED_KEY_BYTES': environ.get('BCRYPT_DESIRED_KEY_BYTES', 32),
    'BCRYPT_ROUNDS': 12
}
