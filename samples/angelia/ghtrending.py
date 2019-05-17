# -*- coding: utf8 -*-

import botutils
import datetime
import bs4
import logging
import os


class GHTrending(botutils.Robot):
    """ 抓取Github Trending（daily）"""

    def __init__(self, config):
        super().__init__(config)
        self._daily_log = os.path.join(self._config_path(), 'ght-daily.cache')

    def publish(self):
        if not self.is_today_published():
            super().publish()
            self.mark_today_published()
        else:
            logging.debug('has published today')

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

    def _crawl(self):
        logging.debug('publish github-trending')
        result = self.__daily_trending()
        for item in result:
            msg = self.__to_msg(item)
            yield msg

    def __daily_trending(self):
        url = 'https://github.com/trending?since=daily'

        data = botutils.get(url)
        soup = bs4.BeautifulSoup(data, 'lxml')

        trending = []
        for li in soup.select('.repo-list li'):
            div_list = li.find_all('div')
            data = {}
            data['title'] = div_list[0].get_text().strip()
            data['link'] = 'https://github.com' + \
                div_list[0].select_one('a').get('href')
            data['desc'] = div_list[2].get_text().strip()

            lang_color_span = div_list[3].select_one('.repo-language-color')
            if lang_color_span is None:
                data['lang'] = None
            else:
                data['lang'] = lang_color_span.find_next_sibling(
                    'span').string.strip()
            data['star'] = div_list[3].find_all('a')[0].get_text().strip()

            today_start_svg = div_list[3].select_one('span > svg')
            if today_start_svg is None:
                data['today_star'] = '0'
            else:
                data['today_star'] = today_start_svg.next_sibling.string.strip()
            data['folk'] = div_list[3].find_all('a')[1].get_text().strip()

            # data['update'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data['update'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            trending.append(data)
        return trending

    def __to_msg(self, item):
        msg = botutils.MessageItem(guid=item['title'])
        msg.title = '%s %s' % (
            item['title'], '(' + item['lang'] + ')' if item['lang'] is not None else '')
        msg.channel = 'daily trending'
        msg.link = item['link']
        msg.update = item['update']
        msg.desc = '%s\nstar: %s(%s)\nfolk: %s' % (
            item['desc'], item['star'], item['today_star'],  item['folk'])
        return msg
