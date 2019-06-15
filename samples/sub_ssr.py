# -*- coding:utf-8 -*-

import sys
import requests
import base64


def safe_b64decode(data):
    data = data + '='*(4-len(data))
    return base64.b64decode(data)

def get_sub_ssr(url):
    b64content = requests.get(url).text
    content = safe_b64decode(b64content).decode()
    return content.split()

def repack(ssr_list):
    repack_list = []
    for ssr in ssr_list:
        param = safe_b64decode(ssr[6:]).decode()+'&protoparam=&obfsparam='
        repack_ssr = 'ssr://'+base64.b64encode(param.encode()).decode()
        repack_list.append(repack_ssr)
    return repack_list

def subscribe(url):
    ssr_list = get_sub_ssr(url)
    repack_list = repack(ssr_list)
    repack_content = '\n'.join(repack_list)
    return base64.b64encode(repack_content.encode()).decode()

if __name__ == '__main__':
    # sub_url = sys.argv[1]
    sub_url = 'https://api.st.link/sss/nasa/c3269c34'
    ssr_list = get_sub_ssr(sub_url)
    repack_list = repack(ssr_list)
    print('\n\n'.join(repack_list))
    
