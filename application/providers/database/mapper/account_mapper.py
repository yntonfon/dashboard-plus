from sqlalchemy import Column, Integer, String, Boolean

from application.providers.database import BaseMapper


class AccountMapper(BaseMapper):
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
