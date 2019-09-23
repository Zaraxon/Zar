import sys
import qrcode
from PIL import Image


def QR_code(str_in):
    try:
        img = qrcode.make(str_in)
        img.save('trans.png')
    except BaseException:
        print('输入有误，请正确输入！')
