import base64


def Encoding(str_in):
    try:
        str_in = str_in.encode('utf-8')
        str_in_code = base64.b64encode(str_in)
        str_in_code = str(str_in_code)
        str_in_code = str_in_code.strip('b\'')
        print("加密后的字符串为 ", str_in_code, "\n")
    except BaseException:
        print("输入有误，请进行合法输入\n")


def Decoding(str_in):
    try:
        str_in = str_in.encode('utf-8')
        str_in_code = base64.b64decode(str_in)
        str(str_in_code, encoding='utf-8')
        print("解密后的字符串为 ", str_in_code, "\n")
    except BaseException:
        print("解密失败，请进行合法输入")
