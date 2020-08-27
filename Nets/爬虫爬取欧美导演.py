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
    pattern = re.compile('<li class="none" num=".*?>(\d*).<a href="#" onclick="return false;">(.*?)</a></li>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            '排名': item[0].strip(),
            '欧美导演': item[1].strip()
        }

def write_to_file(content):
    with open('result of 欧美导演.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main():
    url = 'http://movie.mtime.com/list/45.html'
    html = get_one_page(url)

    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()  # 每页25个电影信息