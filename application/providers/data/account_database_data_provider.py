from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import PersitenceException, EntityAlreadyExistsException
from application.core.port.insert_account_port import InsertAccountPort
from application.providers.data import DatabaseAccessLayer
from application.providers.data.account_data_mapper import AccountMapper


class AccountDatabaseDataProvider(InsertAccountPort):
    def __init__(self, db: DatabaseAccessLayer):
        self.db = db

    def insert(self, account):
        new_account = AccountMapper(
            username=account.username,
            email=account.email,
            hash_password=account.hash_password,
            email_confirmed=account.email_confirmed
        )
        self.db.session.add(new_account)

        try:
            self.db.session.commit()
        except IntegrityError:
            raise EntityAlreadyExistsException(name=Account.__name__, keys=('email',))
        except SQLAlchemyError as error:
            raise PersitenceException(origins=error)
        else:
            return new_account.id