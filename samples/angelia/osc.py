# -*- coding: utf8 -*-

import dailybot
import botutils
import datetime
import bs4
import logging
import os


class OSChina(dailybot.DailyRobot):
    """
    爬取开源中国每日资讯
    """

    def __init__(self, config):
        super().__init__(config)
        self._daily_log = os.path.join(self._config_path(), 'osc-daily.cache')

    def _crawl(self):
        logging.debug('publish osc-news')
        return self._news()

    def _news(self):
        url = 'https://www.oschina.net/news/widgets/_news_index_all_list?p=%s&type=ajax'

        page = 1
        messages = []
        while True:
            is_lastpage, page_messages = self._page_to_items(url % page)
            if not page_messages:
                break
            else:
                page += 1
                messages.extend(page_messages)
                if is_lastpage:
                    break
        return messages

    def _page_to_items(self, url):
        """抓取一页数据
        :param url: 新闻页面url
        :return (is_lastpage, messages): 是否是最后一页，本页所有数据´
        """
        data = botutils.get(url, headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        })
        soup = bs4.BeautifulSoup(data, 'lxml')

        items = soup.select('.news-item')
        messages = []
        is_lastpage = False
        for item in items:
            header = item.select_one('.header')
            if not header:
                continue

            desc = item.select_one('.description')
            extras = item.select_one('.extra').select('.item')

            update_date = extras[1].get_text().strip()
            if not update_date.startswith('今天'):
                is_lastpage = True
                break

            title = header.select_one('a').get_text().strip()
            msg = botutils.MessageItem(guid=title)
            msg.title = title
            msg.link = header.select_one('a').get('href').strip()
            msg.desc = desc.get_text().strip()
            msg.update = update_date.replace(
                '今天', datetime.datetime.now().strftime('%Y-%m-%d'))
            msg.channel = extras[0].get_text().strip()

            messages.append(msg)
        return is_lastpage, messages
