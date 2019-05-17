# -*- coding: utf8 -*-

import botutils
import datetime
import bs4
import logging
import os


class DailyRobot(botutils.Robot):
    """ 抓取Github Trending（daily）"""

    def __init__(self, config):
        super().__init__(config)
        self._daily_log = os.path.join(
            self._config_path(), '%s.cache' % self.__class__.__name__)

    def publish(self):
        if not self.is_today_published():
            super().publish()
            self.mark_today_published()
        else:
            logging.debug('%s has published today' % self.__class__.__name__)

    def is_today_published(self):
        if not os.path.exists(self._daily_log):
            return False
        is_pub = False
        with open(self._daily_log, 'r') as f:
            last_date = f.readline().strip()
            is_pub = last_date == datetime.datetime.now().strftime('%Y-%m-%d')
        return is_pub

    def mark_today_published(self):
        last_date = datetime.datetime.now().strftime('%Y-%m-%d')
        with open(self._daily_log, 'w') as f:
            f.write(last_date)
