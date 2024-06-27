import csv
from pymongo import MongoClient


#创建MongoDB客户端
client = MongoClient('mongodb://192.168.3.31:27017/')

#连接到数据库
db = client['bsds']  # 替换为你的数据库名

#获取所有集合的对象
collection_names = db.list_collection_names()
# 指定要写入CSV的字段和对应的标题
csv_headers = ['id', 'userId', 'url', 'createTime', 'ip', 'userAgent', 'requestTime', 'behavior']
#csv_headers = ['id', 'createTime', 'behavior']

for collection_name in collection_names:
    #获取集合对象
    collection = db["service_log_2024-06-27"]

    # 执行查询操作
    data = collection.find({"systemId": "1797644612455555073", 'userId': "步卓伦"},
                           {'behavior': 1,
                            'createTime': 1,
                            'ip': 1,
                            'requestTime': 1,
                            'url': 1,
                            'userAgent': 1,
                            'userId': 1})

    # 创建一个CSV文件并写入数据
    with open('data/data_2024_06_27.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
        for item in data:
            writer.writerow(list(item.values()))  # 写入数据行
