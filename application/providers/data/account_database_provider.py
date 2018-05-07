from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from application.core.entity.account import Account
from application.core.exception.dashboardplus_exception import PersitenceException, EntityAlreadyExistsException
from application.core.usecase.insert_account_port import InsertAccountPort

URL = 'sqlite:///:dashboard-plus:'

Base = declarative_base()


class AccountMapper(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    hash_password = Column(String)
    email_confirmed = Column(Boolean)

    def __repr__(self):
        return "<Account(username={0}, email={1}, hash_password={2}, email_confirmed={3})>".format(
            self.username, self.email, self.hash_password, self.email_confirmed
        )


class AccountDatabaseDataProvider(InsertAccountPort):
    def insert(self, account):
        new_account = AccountMapper(
            username=account.username,
            email=account.email,
            hash_password=account.hash_password,
            email_confirmed=account.email_confirmed
        )
        session = Session()
        session.add(new_account)

        try:
            session.commit()
        except IntegrityError:
            raise EntityAlreadyExistsException(name=Account.__name__, keys=('email',))
        except SQLAlchemyError as error:
            raise PersitenceException(origins=error)
        else:
            return new_account.id


engine = create_engine(URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
