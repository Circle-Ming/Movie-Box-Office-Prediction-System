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
    pattern = re.compile('hd.*?"pos".*?(\d*)</span>.*?class="title".*?_blank.*?>\n(.*?)</a>'
                         + '.*?rating_nums">(.*?)</span>.*?abstract">.*?:(.*?)<br />.*?:(.*?)<br />.*?:(.*?)<br />.*?:(.*?)<br />.*?:(.*?)</div>.*?'
                         + '"comment">.*?</span>总票房：(.*?)万元.*?上映日期：(.*?) .*?发行类别：(.*?)</blockquote>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            '电影名': item[1].strip(),  # string.strip()不加参数的话可以直接就将空格\n\r等过滤掉
            '评分': item[2].strip(),
            '导演': item[3].strip(),
            '主演': item[4].strip(),
            '类型': item[5].strip(),
            '制片国家/地区': item[6].strip(),
            '年份': item[7].strip(),
            '票房': item[8].strip(),
            '上映日期': item[9].strip(),
            '发行类别': item[10].strip()
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(start):
    url = 'https://www.douban.com/doulist/1295618/?start=' + str(start) + '&sort=seq&sub_type= '
    html = get_one_page(url)

    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(39):  # 共39个豆瓣网页
        main(i * 25)  # 每页25个电影信息