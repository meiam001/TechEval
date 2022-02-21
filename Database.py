from sqlalchemy import Column, \
    Integer, String, ForeignKey, Table, \
    DATETIME, create_engine, MetaData, Float, DateTime
from sqlalchemy.orm import Session
import time
from sqlalchemy.ext.declarative import declarative_base
import os
Base = declarative_base()

class ConnectDB:
    DB_ENGINE = {
        'sqlite': 'sqlite:///{DB}'
    }
    db_engine = None
    database_folder = 'Database'

    def __init__(self, dbtype='sqlite', dbname='.\\Database\\3siDatabase.db', username='', password=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url, connect_args={'timeout': 20,
                                                                     'check_same_thread': False})
        else:
            print("DBType is not found in DB_ENGINE")

    @staticmethod
    def get_session(engine):
        return Session(engine)

class Problem1(Base):
    __tablename__='problem1'
    rowno = Column(Float, primary_key=True)
    float1 = Column(Float)
    word1 = Column(String)
    float2 = Column(Float)
    int1 = Column(Integer)
    word2 = Column(String)

class MyDatabase(ConnectDB):

    def __init__(self, dbtype='sqlite', dbname='.\\Database\\3siDatabase.db', username='', password=''):
        """
        Data layer for interacting with database
        :param dbtype: Currently only support sqlite
        :param dbname: database name
        :param username: username for database
        :param password: password for database
        """
        super().__init__(dbtype, dbname, username, password)

    def create_db_tables(self):
        """
        Creates tables if they don't exist
        MUST MATCH TABLE OBJECTS DEFINED ABOVE
        :return:
        """
        self.create_folder('.', 'Database')
        metadata = MetaData()

        problem1 = Table('problem1', metadata,
        Column('rowno', Float, primary_key=True),
        Column('float1', Float),
        Column('word1', String),
        Column('float2',Float),
        Column('int1', Integer),
        Column('word2', String)
        )
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    def create_folder(self, path: str, folder_name: str):
        """
        creates database folder
        :param path: full path leading to folder
        :param folder_name: folder name
        :return:
        """
        if folder_name not in os.listdir(path):
            os.mkdir(f'{path}\\{folder_name}')

    def insert_df(self, session, df, mapper, *args):
        rows = []
        t1 = time.time()
        for row in df.itertuples():
            current_row = {arg: getattr(row, arg) for arg in args}
            rows.append(current_row)
            if len(rows) % 100000 == 0 and len(rows) != 0:
                print('100k down')
                session.bulk_insert_mappings(mapper, rows)
                rows = []
        session.bulk_insert_mappings(mapper, rows)
        session.commit()
        print(f'Done! Took {time.time() - t1} seconds!')

if __name__=='__main__':
    x = MyDatabase('sqlite', dbname='.\\Database\\3siDatabase.db')
    sesh = x.get_session(x.db_engine)
    x.create_db_tables()