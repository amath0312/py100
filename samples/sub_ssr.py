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

def repack(ssr_list, b64_fmt=False):
    repack_list = []
    for ssr in ssr_list:
        param = safe_b64decode(ssr[6:]).decode()+'&protoparam=&obfsparam='
        param = safe_param(param)
        repack_ssr = ''
        if b64_fmt:
            repack_ssr = 'ssr://'+base64.b64encode(param.encode()).decode()
        else:
            repack_ssr = 'ssr://'+param
        repack_list.append(repack_ssr)
    return repack_list

def safe_param(param):
    host, port, fmt, encmode, confuse, pwd_and_others = param.split(':')
    
    pwd = pwd_and_others[0:pwd_and_others.index('/?')]
    pwd = pwd.rstrip('=')
    queries = pwd_and_others[pwd_and_others.index('/?')+2:]
    simple_queries = 'group='+base64.b64encode('st-link'.encode()).decode().rstrip('=')
    for entry in queries.split('&'):
        key = entry[:entry.index('=')]
        value = entry[entry.index('=')+1:]
        value = value.rstrip('=')
        simple_queries = simple_queries + "&" + key+"="+value


    return host+':'+port+':'+fmt+':'+encmode+':'+confuse+':'+pwd+'/?'+simple_queries


def subscribe(url):
    ssr_list = get_sub_ssr(url)
    repack_list = repack(ssr_list)
    repack_content = '\n'.join(repack_list)
    return base64.b64encode(repack_content.encode()).decode()

def subscribe_simple_fmt(url):
    ssr_list = get_sub_ssr(sub_url)
    repack_list = repack(ssr_list, b64_fmt=False)
    return '\n\n'.join(repack_list)

def subscribe_b64_fmt(url):
    ssr_list = get_sub_ssr(sub_url)
    repack_list = repack(ssr_list, b64_fmt=True)
    return '\n\n'.join(repack_list)

if __name__ == '__main__':
    # sub_url = sys.argv[1]
    sub_url = 'https://api.st.link/sss/nasa/c3269c34'
    print(subscribe_b64_fmt(sub_url))

    
