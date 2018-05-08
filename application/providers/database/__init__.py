from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = 'sqlite:///:dashboard-plus:'

BaseMapper = declarative_base()


class DatabaseAccessLayer:
    engine = None
    conn_string = URL
    base_mapper = BaseMapper
    session = None

    def db_init(self, conn_string: str, log: bool):
        self.engine = create_engine(conn_string or self.conn_string, echo=log or False)
        self.base_mapper.metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def db_drop(self):
        self.base_mapper.metadata.drop_all(bind=self.engine)
