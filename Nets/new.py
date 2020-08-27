import requests
from requests.exceptions import RequestException
import re  # re模块 正则表达式
import json

# from multiprocessing import Pool

def get_one_page(url: object) -> object:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<td style.*?width:150px.*?>(.*?)</td>.*?>(.*?)</td>.*?>(.*?)%</td>.*?>(.*?)</td>.*?>(.*?)%</td>.*?>(.*?)</td>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            '电影名': item[0].strip(),  # string.strip()不加参数的话可以直接就将空格\n\r等过滤掉
            '实时票房（万）': item[1].strip(),
            '票房占比%': item[2].strip(),
            '累计票房（万）': item[3].strip(),
            '排片占比': item[4].strip(),
            '上映天数': item[5].strip()
        }


def write_to_file(content):
    with open('result of whole.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main():
    url = 'http://www.cbooo.cn'
    html = get_one_page(url)

    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()

import os
files = os.listdir("C:/Users\wanghuiming\Desktop\Python\CNN")
for filename in files:
    portion = os.path.splitext(filename)
    print(portion)
    if portion[1] ==".txt"and portion[0] == "result of whole":
        newname = portion[0]+".json"
        os.chdir("C:/Users\wanghuiming\Desktop\Python\CNN")
        os.rename(filename,newname)


import json
data = []
filename  = 'result of whole.json'
with open(filename,"rb") as f:
    for line in f:
        data.append(json.loads(line))
str = "\r\n"
for item in data:
    str = str + "%s,%s,%s,%s,%s,%s\r\n" % (item["电影名"],item["实时票房（万）"],item["票房占比%"],item["累计票房（万）"],item["排片占比"],item["上映天数"])
import codecs
username = 'result of whole.csv'
file_object = codecs.open(username, 'w' ,encoding = "utf8")
file_object.write(str)
file_object.close()
print ("success")



