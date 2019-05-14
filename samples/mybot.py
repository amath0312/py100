# -*- coding: utf8 -*-

from urllib import request
import bs4
import ssl
import json
import time
import sys
import pyqrcode
import qrcode
import datetime
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def post(url, json_data):
    headers = {"Content-Type": "application/json"}
    ctx = ssl.SSLContext()
    data_json = json.dumps(json_data)
    logging.debug('send: %s', data_json)

    req = request.Request(url=url,
                          headers=headers, data=data_json.encode('utf-8'))
    resp = request.urlopen(req, timeout=10, context=ctx)
    data = resp.read().decode("utf-8")
    
    logging.debug('receive: %s', data)
    return json.loads(data)


def heartbeat(code):
    param = {"code": code}
    url = "https://api.st.link/angelia/heartbeat"
    data = post(url, param)
    errcode = data['errcode']
    return errcode


def publish(code, token, message, link=''):
    param = {
        'code': code,
        'token': token,
        'message': message,
        'link': link
    }
    url = "https://api.st.link/angelia/botpublish"
    data = post(url, param)
    errcode = data['errcode']
    return errcode


def print_help(actions):
    for act in actions:
        print(act, ':', actions[act])
    print()


def test_bot(config):
    actions = {
        'b': 'send heart beat',
        'm': 'send message',
        's': 'make bot qrcode for share',
        'q': 'quit'
    }
    print_help(actions)

    while True:
        action = input('choice: ')
        action = action.lower()

        if action == 'b':
            errcode = heartbeat(config['code'])
            if errcode == 0:
                print("heart beat success")
            else:
                print('heart beat fail, ', errcode)
        elif action == 'm':
            msg = input('input message: ')
            errcode = publish(config['code'], config['token'], msg)
            if errcode == 0:
                print("send message success")
            else:
                print('send message fail, ', errcode)
        elif action == 's':
            bot_code = input('input bot code: ')
            # img = pyqrcode.create(content=bot_code, version=1)
            # print(img.terminal(quiet_zone=1))
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(bot_code)
            qr.make(fit=True)
            qr.print_ascii(out=sys.stdout)
            qr.make_image()
        elif action == 'q':
            break
        else:
            print_help(actions)

    print("exit.")


def github_daily_trending():
    url = 'https://github.com/trending?since=daily'
    ctx = ssl.SSLContext()
    req = request.Request(url=url)
    resp = request.urlopen(req, timeout=10, context=ctx)
    data = resp.read().decode('utf-8')
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


def trend_item_str(item):
    text = '[daily trending]\n' + item['title'] + ((' (' + item['lang'] + ')')
                                                   if item['lang'] is not None else '') + '\n'
    text = text + '[更新于 ' + item['update'] + ' ]\n'
    text = text + item['desc'] + '\n'
    text = text + \
        'star: %s(%s)' % (item['star'], item['today_star']) + '\n'
    text = text + 'folk: ' + item['folk']
    return (text, item['link'] if item['link'] is not None else '')


if __name__ == "__main__":
    config = {
        'token': "4044a4fe7a0437838d1003f3fb369367",
        'code': "f188414a716611e9a4ca3663a0d9922f"
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_bot(config)
    else:
        result = github_daily_trending()
        heartbeat(config['code'])
        for item in result:
            msg, link = trend_item_str(item)
            publish(config['code'], config['token'], msg, link)
            logging.debug('%s\n%s\n[%s]\n', '=' * 80, msg, link)
