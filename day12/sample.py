# -*- coding:utf8 -*-
import re


def verify_user(username, qq):
    """
    验证输入用户名和QQ号是否有效并给出对应的提示信息
    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
    """
    is_name_valid = verify_name(username)
    is_qq_valid = verify_qq(qq)
    if is_name_valid and is_qq_valid:
        return '验证成功'
    elif is_name_valid and not is_qq_valid:
        return '请输入有效的qq号'
    elif not is_name_valid and is_qq_valid:
        return '请输入有效的用户名'
    else:
        return '请输入有效的用户名和qq号'


def verify_qq(qq):
    """
    验证输入QQ号是否有效
    要求：QQ号是5~12的数字且首位不能为0
    """
    pattern = r'^[1-9]\d{4,11}$'
    return True if re.match(pattern, qq) else False


def verify_name(username):
    """
    验证输入用户名是否有效
    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    """
    pattern = r'[a-zA-Z0-9_]{6,20}'
    return True if re.match(pattern, username) else False


def pickup_tels1(sentence):
    # 1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8}
    pattern = r'(?<=\D)((13\d|14[57]\d{8}|15[0-35-9]|17[678]|18\d)(\d{8}))(?=\D)'
    tel_list = re.findall(pattern, sentence)
    return tel_list


def pickup_tels2(sentence):
    tel_list = []

    pattern = re.compile(
        r'(?<=\D)(?P<tel>(?P<pre>13\d|14[57]\d{8}|15[0-35-9]|17[678]|18\d)(?P<loc>\d{4})(?P<num>\d{4}))(?=\D)')
    m = pattern.search(sentence)
    while m:
        tel_list.append({
                'tel': m.group('tel'),
                'prefix': m.group('pre'),
                'location_code': m.group('loc'),
                'number': m.group('num'),
            })
        m = pattern.search(sentence, m.end())
    return tel_list

def purify(sentence):
    pattern = '[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔'
    return re.sub(pattern, '*', sentence, flags=re.IGNORECASE)

def split_str(sentence):
    pattern = r'[,.，。]'
    splits = re.split(pattern, sentence)
    splits = [s for s in splits if s != '']
    return splits

def main():
    print(verify_user('abcdefg', '10000'))
    print(verify_user('啊啊啊啊啊啊啊', '10000'))
    print(verify_user('abcdefg', '00000'))
    print(verify_user('啊啊啊啊啊啊啊', '00000'))
    sentence = """
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    """
    tel_list = pickup_tels2(sentence)
    print(tel_list)
    for tel in tel_list:
        print(tel, type(tel))
    
    print(purify('你丫是傻叉吗? 我操你大爷的. Fuck you.'))
    print(split_str('窗前明月光，疑是地上霜。举头望明月，低头思故乡。'))


if __name__ == "__main__":
    main()
