from os import environ


def get_int(var, default):
    return int(environ.get(var, default))


def get_bool(var, default):
    return bool(environ.get(var, default))


default_config = {
    'SECRET_KEY': environ.get('SECRET_KEY', 'secret_for_test'),
    'BCRYPT_DESIRED_KEY_BYTES': get_int('BCRYPT_DESIRED_KEY_BYTES', 32),
    'BCRYPT_ROUNDS': get_int('BCRYPT_DESIRED_KEY_BYTES', 100),
    'DATABASE_URL': environ.get('DATABASE_URL', 'sqlite:////tmp/:dashboard-plus:'),
    'DATABASE_LOGGER_ACTIVE': get_bool('DATABASE_LOGGER_ACTIVE', False)
}
