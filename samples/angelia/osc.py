# -*- coding: utf8 -*-

import botutils
import datetime
import bs4
import logging
import os

class OSChina(botutils.Robot):
    """
    爬取开源中国每日资讯
    """

    def __init__(self, config):
        super().__init__(config)
        self._daily_log = os.path.join(self._config_path(), 'osc-daily.cache')

    def _crawl(self):
        logging.debug('publish github-trending')
        msg = botutils.MessageItem(guid='1', title='测试消息', desc='#消息内容#', update='2019-05-01 12:00', channel='oschina', link='https://www.oschina.net')
        return [msg]