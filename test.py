import time
import pymongo
import threading
from bson import ObjectId

Path = r'C:\Users\LIU\Desktop\C0.txt'
client = pymongo.MongoClient('mongodb://root:123456@192.168.3.6:27017/')

db = client["剑南春A2020226"]
col1 = db["A2020226内码"]
col2 = db["A2020226外码"]
col3 = db["A2020226内码单检测"]
col4 = db["A2020226外码单检测"]
col5 = db["A2020226关联检测"]
#
MyList = list()
with open(Path, 'r') as fo:
    Data = fo.readlines()
print('文件读取完成')

for i in Data:
    LineDict = {'_id': i}
    MyList.append(LineDict)
m1 = MyList[0:1000000]
m2 = MyList[1000000:2000000]
m3 = MyList[2000000:3000000]
m4 = MyList[3000000:4000000]
m5 = MyList[4000000:5000000]


def func(i):
    x = eval('col' + str(i+1)).insert_many(eval('m' + str(i+1))).inserted_ids


print('数据整理完成')
S = time.perf_counter()
for i in range(5):
    try:
        t = threading.Thread(target=func, args=(i,))
        t.setDaemon(True)  # 把子进程设置为守护线程，必须在start()之前设置
        t.start()
        t.join()
    # x = col3.insert_many(MyList).inserted_ids
    # x = col4.insert_many(MyList).inserted_ids
    # x = col5.insert_many(MyList).inserted_ids
    # x = col6.insert_many(MyList).inserted_ids
    except pymongo.errors.BulkWriteError as e:
        print(e.details['writeErrors'][0]['keyValue'], '重复')

E = time.perf_counter()
print(E - S)

# c = 0
# for i in range(4):
#     c += 1
#     MyList = []
#     for line in Data:
#         lines = line + str(c)
#         LineDict = {"_id": lines, "alexa": "100", "url": "https://www.taobao.com"}
#         MyList.append(LineDict)
#     S = time.perf_counter()
#     print('数据整理完成')
#     try:
#         x = col2.insert_many(MyList)
#     except pymongo.errors.BulkWriteError as e:
#         print(e.details['writeErrors'][0]['keyValue'], '重复')
#     E = time.perf_counter()

# for col in [col2]:
#   count = col.estimated_document_count()
#   print(count)
#   s = time.perf_counter()
#   Data = col.find({'_id':'http://q.tanjiu.cn/t/?g=b86e197224c3ba0.07213359373066341\n1'})
#   e = time.perf_counter()
#   for i in Data:
#     print(i,  e-s)
# client.close()
