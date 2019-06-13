# -*- coding: utf8 -*-

import time
import sys
import pyqrcode
import qrcode
import datetime
import multiprocessing
import logging
import botutils
import ghtrending
import osc

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def main():
    config = {
        'ghtrending': {
            'token': "4044a4fe7a0437838d1003f3fb369367",
            'code': "f188414a716611e9a4ca3663a0d9922f"
        },
        'osc': {
            'code': 'T34FYG',
            'token': '8440bf8dd9683b3986a7bab5b7970af8'
        }
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'console':
        test_bot(config)
    elif len(sys.argv) > 1 and sys.argv[1] == 'test':
        # botutils.post('https://api.st.link/angelia/sendmessage/{}/{}/{}'.format(
            # config['code'], config['token'], 'only_for_test'))
        # osc.OSChina(config['osc']).publish()
        import json
        for i in range(40000, 10**6):
            try:
                data = json.dumps({
                    "userid": "emmm_"+str(i).rjust(10,'0'),
                    "code": "ffddedc070d611e9a0253a8dfd6ffffa",
                    "sign": True,
                    "page": 0
                })
                print(data)
                # ret = botutils.post(url='https://api.st.link/angelia/botshop',
                # headers={"Content-Type": "application/json"}, data=data, resp_encoding='utf-8')
                ret = botutils.post(url='https://api.st.link/angelia/follow',
                                    headers={"Content-Type": "application/json"}, data=data, resp_encoding='utf-8')
                print(json.loads(ret))
            except:
                print('error')
    else:
        start = time.time()
        p1 = multiprocessing.Process(target=ghtrending.GHTrending(
            config['ghtrending']).publish, args=())
        p2 = multiprocessing.Process(
            target=osc.OSChina(config['osc']).publish, args=())
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        end = time.time()
        print('time:  %.2f s' % (end-start))


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
            errcode = botutils.heartbeat(config['code'])
            if errcode == 0:
                print("heart beat success")
            else:
                print('heart beat fail, ', errcode)
        # elif action == 'm':
        #     msg = input('input message: ')
        #     errcode = publish(config['code'], config['token'], msg)
        #     if errcode == 0:
        #         print("send message success")
        #     else:
        #         print('send message fail, ', errcode)
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


if __name__ == "__main__":
    main()
