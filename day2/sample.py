import math


def celsius_to_fahrenheit(celsius):
    """
    摄氏度转换成华氏度
    """
    return 1.8 * celsius + 32


def fahrenheit_to_celsius(fah):
    """
    华氏度转摄氏度
    """
    return (fah - 32) / 1.8


def calc_perimeter(radius):
    """
    计算圆周长
    """
    return 2 * math.pi * radius


def calc_area(radius):
    """
    计算圆面积
    """
    return math.pi * radius**2


def is_leap_year(year):
    """
    是否是闰年
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


if __name__ == '__main__':
    # celsius = 37.5
    # print('%.2f℃ = %.2f℉' % (celsius, celsius_to_fahrenheit(celsius)))
    # fah = 120
    # print('%.2f℉ = %.2f℃' % (fah, fahrenheit_to_celsius(fah)))

    # radius = float(input('radius='))
    # print("周长=%.2f\n面积=%.2f" % (calc_perimeter(radius), calc_area(radius)))

    year = int(input('year='))
    print("%d%s闰年" % (year,  '是' if is_leap_year(year) else '不是'))
