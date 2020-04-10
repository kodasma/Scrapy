# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class AmazonPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'bakascrapy',
            database = 'amazonbooks'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books""")
        self.curr.execute("""CREATE TABLE books(
                        title text,
                        author text,
                        imagelink text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO books VALUES (%s, %s, %s)""", (
            item['product_name'][0],
            item['product_author'][0],
            item['product_imagelink'][0]
        ))
        self.conn.commit()