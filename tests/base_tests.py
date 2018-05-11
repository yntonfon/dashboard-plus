import pytest

from application.configuration import config
from application.configuration.ioc_database import IOCDatabase
from tests.common import patch_url_if_xdist


class DatabaseTest:
    def setup_method(self):
        self.db = IOCDatabase.db()
        self.config = config()
        self.config.update({
            'DATABASE_URL': 'sqlite:////tmp/:test-dashboard-plus:',
            'DATABASE_LOGGER_ACTIVE': True
        })
        self.db.init_db(
            conn_string=patch_url_if_xdist(self.config['DATABASE_URL']),
            log=self.config['DATABASE_LOGGER_ACTIVE'])

    def teardown_method(self):
        self.db.session.rollback()
        self.db.clear_db()

@pytest.mark.integration_test
class IntegrationTest(DatabaseTest):
    pass


@pytest.mark.e2e_test
class E2ETest(DatabaseTest):
    pass


@pytest.mark.unit_test
class UnitTest:
    pass
