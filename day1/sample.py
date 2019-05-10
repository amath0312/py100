'''
第一个练习

Version: 0.1
Author: emmm
'''

def print_version_data():
    """
    控制台打印版本信息(version, version_info)
    """
    import sys

    line_size = 100
    print('|' + '-' * (line_size - 2) + '|')
    print(parse_version_data('version-info', str(sys.version_info), 100))
    print('|' + '-' * (line_size - 2) + '|')
    print(parse_version_data('version', str(sys.version), 100))
    print('|' + '-' * (line_size - 2) + '|')

def parse_version_data(keyword, data, line_size):
    """
    解析version参数并进行格式化
    """
    keyword_line = '|' + ' ' * 2 + keyword + ' ' * 4 + ':' + ' ' * \
        (line_size - 1 - 2 - len(keyword) - 4 - 1 - 3) + '--|'
    data_lines = [('|--' + ' ' * 8 + s) for s in data.split('\n')]
    parsed_lines = [s + ' ' * (line_size - len(s) - 3) +
                    '--|' for s in data_lines]
    return keyword_line + '\n' + '\n'.join(parsed_lines)


def test_turtle():
    import turtle
    import random
    
    colors = ['red', 'yellow', 'blue']
    for i in range(3):
        turtle.pensize(random.randrange(3,6))
        turtle.pencolor(random.choice(colors))
        turtle.forward(100)
        turtle.right(180-60)

    turtle.mainloop()
        

if __name__ == '__main__':
    print_version_data()
    print('\n'*3)
        
    import this
    print('\n'*3)

    test_turtle()

