# -*- coding: utf8 -*-

from urllib import request
from urllib.parse import urlencode, quote
import bs4
import ssl
import json
import logging
import os


class Robot(object):

    def __init__(self, config):
        self._token = config.get('token')
        self._code = config.get('code')

    def publish(self):
        messages = self._crawl()
        if messages is not None:
            self.heartbeat()
            counter = 0
            for msg in messages:
                self.bot_publish(message=str(msg), link=msg.link)
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

    def _config_path(self):
        return os.path.split(os.path.realpath(__file__))[0]


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


class MessageItem(object):
    _guid = ''
    _channel = ''
    _title = ''
    _update = ''
    _desc = ''
    _link = ''
    _title = ''

    def __init__(self, guid, channel='', title='', update='', desc='', link=''):
        self._guid = guid
        self._channel = channel
        self._title = title
        self._update = update
        self._desc = desc
        self._link = link

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, guid):
        self._guid = guid

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def update(self):
        return self._update

    @update.setter
    def update(self, update):
        self._update = update

    @property
    def link(self):
        return self._link if self._link is not None else ''

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def desc(self):
        return self.desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    def __str__(self):
        line = '\n' + '-' * 25 + '\n'
        text = self._title
        text += line
        text += self._desc
        text += line
        if self._channel is not None and self._channel != '':
            text += self._channel

        if self._update is not None and self._update != '':
            text += ' 更新于 %s' % self._update
        return text
