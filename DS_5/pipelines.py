# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

stuff= {"A", "B", "C"}
stuff2 = '", "'.join(stuff)

print("[{0}]".format('", "'.join(stuff)))

# class Ds5Pipeline(object):
#     def process_item(self, item, spider):
#         return item
