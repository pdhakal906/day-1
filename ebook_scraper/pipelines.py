# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from itemadapter import ItemAdapter
from openpyxl import Workbook


# SAVE TO EXCEL

# class EbookScraperPipeline:
#     def open_spider(self, spider):
#         self.workbook = Workbook()
#         self.sheet = self.workbook.active
#         self.sheet.title = "ebooks"
#         self.sheet.append(spider.cols)


#     def process_item(self, item, spider):
#         self.sheet.append([item['title'], item['price']])

#     def close_spider(self, spider):
#         self.workbook.save('ebooks.xlsx')


# SAVE TO MONGODB

# class EbookScraperPipeline:
#     def open_spider(self, spider):
#         self.client = MongoClient(
#             host= "mongodb+srv://pratik:pratik_dhakal_900@cluster0.kiya07v.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp",
#             connect = False
#         )

#         self.collection = self.client.get_database("ebooks").get_collection("travel")



#     def process_item(self, item, spider):
#         self.collection.insert_one(
#            ItemAdapter(item).asdict()
#         )
        
#     def close_spider(self, spider):
#         self.client.close()
       

class EbookScraperPipeline:
    
    def process_item(self, item, spider):
        return item

