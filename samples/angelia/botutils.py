# -*- coding: utf8 -*-

from urllib import request
from urllib.parse import urlencode, quote
import bs4
import ssl
import json
import logging


class Robot(object):

    def __init__(self, config):
        self._token = config.get('token')
        self._code = config.get('code')

    def publish(self):
        messages = self._crawl()
        if messages is not None:
            self.heartbeat()
            counter = 0
            for msg,link in messages:
                self.bot_publish(message=msg, link=link)
                counter += 1
            logging.debug('publish %d messages' % counter)

    def post_to_bot(self, url, json_data=None):
        headers = {"Content-Type": "application/json"}
        if json_data is not None:
            try:
                data_json = json.dumps(json_data)
            except:
                data_json = None
        else:
            data_json = None
        logging.debug('send: %s, url=%s' % (data_json, url))

        post_data = None if data_json is None else data_json
        data = post(url, headers=headers, data=post_data)

        logging.debug('receive: %s', data)
        return json.loads(data)

    def heartbeat(self):
        param = {"code": self._code}
        url = "https://api.st.link/angelia/heartbeat"
        data = self.post_to_bot(url, param)
        errcode = data['errcode']
        return errcode

    def bot_publish(self, message, link=''):
        param = {
            'code': self._code,
            'token': self._token,
            'message': message,
            'link': link
        }
        url = "https://api.st.link/angelia/botpublish"
        data = self.post_to_bot(url, param)
        errcode = data['errcode']
        return errcode

    def _crawl(self):
        pass


def get(url, headers=None, queries=None, resp_encoding='utf-8'):
    """
    提交post请求
    :param url: 请求地址
    :param headers: 自定义HTTP头
    :param data:请求Body，str类型
    """
    if queries is not None:
        url = url + "?" + urlencode(queries)
    logging.debug('get url: ' + url)
    ctx = ssl.SSLContext()
    headers = {} if headers is None else headers
    req = request.Request(url=url,
                          headers=headers)
    resp = request.urlopen(req, timeout=10, context=ctx)
    resp_data = resp.read().decode(resp_encoding)
    return resp_data


def post(url, headers=None, data=None, resp_encoding='utf-8'):
    """
    提交post请求
    :param url: 请求地址
    :param headers: 自定义HTTP头
    :param data:请求Body，str类型
    """
    ctx = ssl.SSLContext()
    headers = {} if headers is None else headers
    req = request.Request(url=url,
                          headers=headers, data=data.encode('utf-8'), method='POST')
    resp = request.urlopen(req, timeout=10, context=ctx)
    resp_data = resp.read().decode(resp_encoding)
    return resp_data
