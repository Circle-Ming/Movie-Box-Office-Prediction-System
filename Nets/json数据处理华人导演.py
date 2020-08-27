#-*- coding: UTF-8 -*-
import json
data = []
filename  = 'result of 华人导演.json'
with open(filename,"rb") as f:
    for line in f:
        data.append(json.loads(line))
str = "\r\n"
for item in data:
    str = str + "%s,%s\r\n" % (item["排名"],item["华人导演"])
import codecs
username = 'result of 华人导演.csv'
file_object = codecs.open(username, 'w' ,encoding = "utf8")
file_object.write(str)
file_object.close()
print ("success")
