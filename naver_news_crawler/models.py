from sqlalchemy import create_engine, Column, Integer, String, DateTime, UnicodeText, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import datetime
import os

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(url=URL.create(drivername='mysql+mysqldb',
                                        username='truelifer',
                                        password='qkrdmswns1@',
                                        host='truelifer.iptime.org',
                                        port='13306',
                                        database='test'),
                                        # username=os.environ.get('DAUM_NEWS_CRAWLER_DB_USER'),
                                        # password=os.environ.get('DAUM_NEWS_CRAWLER_DB_PW'),
                                        # host=os.environ.get('DAUM_NEWS_CRAWLER_DB_HOST'),
                                        # port=os.environ.get('DAUM_NEWS_CRAWLER_DB_PORT'),
                                        # database=os.environ.get('DAUM_NEWS_CRAWLER_DB')),
                         connect_args={'charset': 'utf8mb4',
                                       'use_unicode': 'True'})


def create_tables(engine):
    DeclarativeBase.metadata.create_all(engine, checkfirst=True)


class Article(DeclarativeBase):
    __tablename__ = 'article'

    id = Column('id', String(50), primary_key=True)
    source = Column('source', String(50), nullable=False, server_default='')
    category = Column('category', String(50), nullable=False, server_default='')
    title = Column('title', String(1000), nullable=False, server_default='')
    editor = Column('editor', String(50), nullable=False, server_default='')
    article = Column('article', UnicodeText, nullable=False)
    created_dt = Column('created_dt', DateTime, nullable=False, server_default=str(datetime.datetime.min))
    updated_dt = Column('updated_dt', DateTime, nullable=False, server_default=str(datetime.datetime.min))
    row_created_dt = Column('row_created_dt', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    row_updated_dt = Column('row_updated_dt', DateTime, nullable=False,
                            server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self):
        self.id = ''
        self.source = ''
        self.category = ''
        self.title = ''
        self.editor = ''
        self.article = ''
        self.created_dt = datetime.datetime.min
        self.updated_dt = datetime.datetime.min


class Image(DeclarativeBase):
    __tablename__ = 'image'

    id = Column('id', String(500), primary_key=True)
    article_id = Column('article_id', String(50), nullable=False, server_default='')
    row_created_dt = Column('row_created_dt', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    row_updated_dt = Column('row_updated_dt', DateTime, nullable=False,
                            server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self):
        self.id = ''
        self.article_id = ''
