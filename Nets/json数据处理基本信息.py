#-*- coding: UTF-8 -*-  
import json
data = []
filename  = 'result of json.json'
with open(filename,"rb") as f:
    for line in f:
        data.append(json.loads(line))
str = "\r\n"
for item in data:
    str = str + "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\r\n" % (item["电影名"],item["评分"],item["导演"],item["主演"],item["类型"],item["制片国家/地区"],item["年份"],item["票房"],item["上映日期"],item["发行类别"])
import codecs
username = 'result of json.csv'
file_object = codecs.open(username, 'w' ,encoding = "utf8")
file_object.write(str)
file_object.close()
print ("success")
