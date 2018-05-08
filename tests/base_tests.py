import pytest

from application.providers.data import DatabaseAccessLayer

URL_DB_TEST = 'sqlite:////tmp/:test-dashboard-plus:'


@pytest.mark.integration_test
class IntegrationTest:
    def setup_class(cls):
        cls.db = DatabaseAccessLayer()
        cls.db.db_init(conn_string=URL_DB_TEST, log=False)

    def teardown_class(cls):
        cls.db.db_drop()


@pytest.mark.unit_test
class UnitTest:
    pass
