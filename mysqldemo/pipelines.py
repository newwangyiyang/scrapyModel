# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class MysqldemoPipeline(object):
    def __init__(self, *args, **kwargs):
        self.connection = pymysql.connect(host='localhost',
                                        user='root',
                                        password='root',
                                        db='test',
                                        charset='utf8mb4',
                                        autocommit=True,
                                        cursorclass=pymysql.cursors.DictCursor)
    def process_item(self, item, spider):
        mingyan = item['mingyan']
        zuoze = item['zuoze']
        ctime = item['ctime']
        uid = item['uid']
        sql = 'insert into demo (`id`, `ctime`, `mingyan`, `zuoze`) values (%s, %s, %s, %s)'
        with self.connection.cursor() as cur:
            cur.execute(sql, (uid, ctime, mingyan, zuoze))
