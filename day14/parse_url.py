
from urllib.parse import urlparse
from urllib.parse import quote


def parse(url):
    return quote(url, safe='/|:|=|?')


if __name__ == "__main__":
    print(parse('https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day14-B/网络应用开发.md#发送短信'))
    print(parse('https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day14-B/网络应用开发.md#发送电子邮件'))
