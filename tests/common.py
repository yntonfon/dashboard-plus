from os import environ


def patch_url_if_xdist(url):
    if environ.get('PYTEST_XDIST_WORKER'):
        url = '%s-%s' % (url, environ.get('PYTEST_XDIST_WORKER'))
    return url
