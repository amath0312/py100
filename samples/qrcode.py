
import os
from PIL import Image
from pyzbar import pyzbar

'''
二维码工具
requirement: Pillow, pyzbar
'''


def decode(file_path):
    img = enhanced_image(file_path)
    barcodes = pyzbar.decode(img, symbols=[pyzbar.ZBarSymbol.QRCODE])
    data_lst = [data.data.decode() for data in barcodes]
    return data_lst


def enhanced_image(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    img = Image.open(file_path)
    
    max_height = 256
    if max_height and img.height > max_height:
        img = img.resize(
            (int(max_height / img.height * img.width), max_height))
    
    return img


if __name__ == '__main__':
    file = '/Users/zhaolin/Desktop/a.jpeg'
    print(decode(file))

    file = '/Users/zhaolin/Desktop/b.png'
    print(decode(file))
