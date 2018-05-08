from os import environ

URL_DB_TEST = 'sqlite:////tmp/test-dashboard-plus'


def get_database_url():
    return _patch_url_if_xdist(URL_DB_TEST)


def _patch_url_if_xdist(url):
    if environ.get('PYTEST_XDIST_WORKER'):
        url = '%s-%s' % (url, environ.get('PYTEST_XDIST_WORKER'))
    return url
