from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = 'sqlite:////tmp/:dashboard-plus:'

BaseMapper = declarative_base()


class DatabaseAccessLayer:
    engine = None
    conn_string = URL
    metadata = BaseMapper.metadata
    session = None

    def init_db(self, conn_string: str, log: bool):
        self.engine = create_engine(conn_string or self.conn_string, echo=log or False)
        self.metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def clear_db(self):
        for table in reversed(self.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.session.commit()
