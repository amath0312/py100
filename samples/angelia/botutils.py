# -*- coding: utf8 -*-

from urllib import request
from urllib.parse import urlencode, quote
import ssl
import json
import os
from abc import ABCMeta, abstractmethod
import logging
import bs4


class Robot(object, metaclass=ABCMeta):

    def __init__(self, config):
        self._token = config.get('token')
        self._code = config.get('code')

    def publish(self):
        messages = self._crawl()
        if messages:
            self.heartbeat()
            counter = 0
            for msg in messages:
                errcode = self.bot_publish(message=str(msg), link=msg.link)
                if errcode != 0:
                    raise PublishError(errcode=errcode, msg=msg)

                counter += 1
            logging.debug('publish %d messages' % counter)

    def post_to_bot(self, url, data=None):
        headers = {"Content-Type": "application/json"}
        if data:
            try:
                data_json = json.dumps(data)
            except:
                data_json = None
        else:
            data_json = None
        logging.debug('send: %s, url=%s' %
                      (data_json.encode('utf-8').decode('unicode_escape'), url))

        post_data = data_json if data_json else None
        resp_data = post(url, headers=headers, data=post_data)

        logging.debug('receive: %s', resp_data)
        return json.loads(resp_data)

    def heartbeat(self):
        """发送机器人心跳检测"""
        param = {"code": self._code, 'sample': '测试'}
        url = "https://api.st.link/angelia/heartbeat"
        data = self.post_to_bot(url, param)
        errcode = data['errcode']
        return errcode

    def bot_publish(self, message, link=''):
        """发送订阅消息"""
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

    @abstractmethod
    def _crawl(self):
        """抓取订阅源并返回消息列表"""
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


def post(url:str, headers:dict=None, data:str=None, resp_encoding:str='unicode_escape', timeout:int=30)->str:
    """
    提交post请求
    :param url: 请求地址
    :param headers: 自定义HTTP头
    :param data:请求Body，str类型
    """
    ctx = ssl.SSLContext()
    headers = {} if headers is None else headers
    req = request.Request(url=url,
                          headers=headers, data=data.encode('utf-8') if data else None, method='POST')
    resp = request.urlopen(req, timeout=timeout, context=ctx)
    resp_data = resp.read().decode(resp_encoding)
    return resp_data


class PublishError(Exception):

    def __init__(self, errcode, msg):
        self.errcode = errcode
        self.msg = msg

    def __str__(self):
        return 'PublishError(%d): %s' % (self.errcode, repr(self.msg))


class MessageItem(object):

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
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    def __str__(self):
        line = '\n' + '-' * 25 + '\n'
        text = self._title
        text += line
        text += self._desc
        text += line
        if self._channel:
            text += self._channel

        if self._update:
            text += ' 更新于 %s' % self._update
        return text

    def __repr__(self):
        return self.__str__()
