import pytest

from application.providers.data import DatabaseAccessLayer
from tests.common import get_database_url


class DatabaseTest:
    def setup_class(cls):
        cls.db = DatabaseAccessLayer()
        cls.db.db_init(conn_string=get_database_url(), log=False)

    def setup_method(cls):
        cls.db.clear()


@pytest.mark.integration_test
class IntegrationTest(DatabaseTest):
    pass


@pytest.mark.integration_test
class E2ETest(DatabaseTest):
    pass


@pytest.mark.unit_test
class UnitTest:
    pass
