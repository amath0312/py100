# -*- coding: utf8 -*-

import time
import sys
import pyqrcode
import qrcode
import datetime
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
        osc.OSChina(config['osc']).publish()
    else:
        ghtrending.GHTrending(config['ghtrending']).publish()
        osc.OSChina(config['osc']).publish()


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
    
