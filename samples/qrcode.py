
import os
from PIL import Image
from pyzbar import pyzbar
import base64

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

    file = '/Users/zhaolin/Desktop/c.jpeg'
    data = decode(file)[0]
    if data.startswith('sub://'):
        print(data)
        data = data[6:data.find('#')]
        data = data + '='*(4-len(data) % 4)
        print(base64.b64decode(data).decode())

    # file = '/Users/zhaolin/Desktop/b.png'
    # print(decode(file))

    file = '/Users/zhaolin/Desktop/nasa-3.jpeg'
    data = decode(file)
    print(data)

    ssr_lst = base64.b64decode('c3NyOi8vWXpoek1TNXFZVzFxWVcxekxtNWxkRG94TURBd05qcHZjbWxuYVc0NllXVnpMVEkxTmkxblkyMDZjR3hoYVc0NlUxWkdWMUpZUm5sWk0xcHdUMEU5UFM4L2NtVnRZWEpyY3oxVWEwWlVVVk13ZUE9PQpzc3I6Ly9Zemh6TWk1cVlXMXFZVzF6TG01bGREb3hNREF3TmpwdmNtbG5hVzQ2WVdWekxUSTFOaTFuWTIwNmNHeGhhVzQ2VTFaR1YxSllSbmxaTTFwd1QwRTlQUzgvY21WdFlYSnJjejFVYTBaVVVWTXdlUT09CnNzcjovL1l6aHpNeTVxWVcxcVlXMXpMbTVsZERveE1EQXdOanB2Y21sbmFXNDZZV1Z6TFRJMU5pMW5ZMjA2Y0d4aGFXNDZVMVpHVjFKWVJubFpNMXB3VDBFOVBTOC9jbVZ0WVhKcmN6MVVhMFpVVVZNd2VnPT0Kc3NyOi8vWXpoek5DNXFZVzFxWVcxekxtNWxkRG94TURBd05qcHZjbWxuYVc0NllXVnpMVEkxTmkxblkyMDZjR3hoYVc0NlUxWkdWMUpZUm5sWk0xcHdUMEU5UFM4L2NtVnRZWEpyY3oxVWEwWlVVVk13TUE9PQpzc3I6Ly9Zemh6TlM1cVlXMXFZVzF6TG01bGREb3hNREF3TmpwdmNtbG5hVzQ2WVdWekxUSTFOaTFuWTIwNmNHeGhhVzQ2VTFaR1YxSllSbmxaTTFwd1QwRTlQUzgvY21WdFlYSnJjejFVYTBaVVVWTXdNUT09CnNzcjovL056UXVNVEl3TGpFM05DNHlORE02TkRRek9tOXlhV2RwYmpwaFpYTXRNalUyTFdkamJUcHdiR0ZwYmpwWmJWbDZUbnBSZWs1VVFYaFBSRkY2VDBkWmVVNVJQVDB2UDNKbGJXRnlhM005VWtWTmVreFZUazlOYVRGQwpzc3I6Ly9PVFV1TVRZNUxqSTJMamt3T2pZMU5UTTFPbTl5YVdkcGJqcGphR0ZqYUdFeU1DMXBaWFJtT25Cc1lXbHVPazFIVm14T1JHc3hUVmRWTlZwdFVtMU5WMGswV21jOVBTOC9jbVZ0WVhKcmN6MVNSVTE2VEZWT1QwMXBNVU09').decode().split()
    print(len(ssr_lst))

    for ssr in ssr_lst:
        if ssr.startswith('ssr://'):
            ssr = 'ssr://'+base64.b64decode(ssr[6:]).decode()+'&protoparam=&obfsparam='
            print(ssr)

    print('ssr://'+base64.b64decode('YzhzMy5qYW1qYW1zLm5ldDoxMDAwNjpvcmlnaW46YWVzLTI1Ni1nY206cGxhaW46U1ZGV1JYRnlZM1pwT0EvP3JlbWFya3M9VGtGVFFTMHomcHJvdG9wYXJhbT0mb2Jmc3BhcmFtPQ==').decode())
    # print('ssr://'+base64.b64decode('OTUuMTY5LjI2LjkwOjY1NTM1Om9yaWdpbjpjaGFjaGEyMC1pZXRmOnBsYWluOk1HVmxORGsxTVdVNVptUm1NV0k0Wmc9PS8/cmVtYXJrcz1SRU16TFVOT01pMUM=').decode())
