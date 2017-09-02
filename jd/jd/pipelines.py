# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs


class JdPipeline(object):
    def __init__(self):
        self.file = codecs.open('/file/jd.json', 'wb')
    def process_item(self, item, spider):
        line = "%s\n" % (item['name'][0].encode('utf-8'))
        self.file.write(line)
        return item

    def spider_closed(self, spider ):
        self.file.close()