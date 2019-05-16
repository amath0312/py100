# -*- coding: utf8 -*-

import botutils
import datetime
import bs4
import logging


class GHTrending(botutils.Robot):

    def _crawl(self):
        logging.debug('publish github-trending')
        result = self.__daily_trending()
        for item in result:
            msg, link = self.__str_item(item)
            yield msg, link

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

    def __str_item(self, item):
        text = '[daily trending] [更新于 ' + \
            item['update'] + ' ]\n' + '-' * 25 + '\n'
        text = text + item['title'] + ((' (' + item['lang'] + ')')
                                       if item['lang'] is not None else '') + '\n'
        text = text + item['desc'] + '\n'
        text = text + \
            'star: %s(%s)' % (item['star'], item['today_star']) + '\n'
        text = text + 'folk: ' + item['folk']
        return (text, item['link'] if item['link'] is not None else '')
