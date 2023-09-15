# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from .models import Article, Image, db_connect, create_tables
import logging

logger = logging.getLogger('naver_news_crawler')


class NaverNewsCrawlerPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        article = Article()
        article.id = item['id'] if item['id'] else ''
        article.source = item['source'] if item['source'] else ''
        article.category = item['category'] if item['category'] else ''
        article.title = item['title'].replace("'", "''") if item['title'] else ''
        article.editor = item['editor'] if item['editor'] else ''

        for i in item['article']:
            article.article += ('\n\n' + i.replace("'", "''"))

        if len(item["created_date"]) == 19:
            article.created_dt = item["created_date"][0:4] \
                                 + '-' \
                                 + item["created_date"][6:8] \
                                 + '-' \
                                 + item["created_date"][10:12] \
                                 + ' ' \
                                 + item["created_date"][14:16] \
                                 + ':' \
                                 + item["created_date"][17:19]

        if len(item["updated_date"]) == 19:
            article.updated_dt = item["updated_date"][0:4] \
                                 + '-' \
                                 + item["updated_date"][6:8] \
                                 + '-' \
                                 + item["updated_date"][10:12] \
                                 + ' ' \
                                 + item["updated_date"][14:16] \
                                 + ':' \
                                 + item["updated_date"][17:19]

        try:
            session.merge(article)

            for i in item['images']:
                image = Image()
                image.id = i
                image.article_id = article.id
                session.merge(image)

            session.commit()
        except Exception as e:
            logger.error('[process_item] error occurred')
            logger.error(str(e))
            session.rollback()
            raise
        finally:
            session.close()

        return item
