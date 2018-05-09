import pytest

from application.configuration import config
from application.configuration.ioc_database import IOCDatabase
from tests.common import patch_url_if_xdist


class DatabaseTest:
    def setup_class(cls):
        cls.db = IOCDatabase.db()
        cls.config = config()
        cls.config.update({
            'DATABASE_URL': 'sqlite:////tmp/:test-dashboard-plus:',
            'DATABASE_LOGGER_ACTIVE': True
        })
        cls.db.init_db(
            conn_string=patch_url_if_xdist(cls.config['DATABASE_URL']),
            log=cls.config['DATABASE_LOGGER_ACTIVE'])

    def setup_method(cls):
        cls.db.clear_db()


@pytest.mark.integration_test
class IntegrationTest(DatabaseTest):
    pass


@pytest.mark.e2e_test
class E2ETest(DatabaseTest):
    pass


@pytest.mark.unit_test
class UnitTest:
    pass
