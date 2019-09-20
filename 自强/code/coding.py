import base64
def ec (s):
    try:
        s=s.encode('utf-16')
        s_code=base64.b64encode(s)
        print("加密后的字符串为 ",s_code,"\n")
    except:
        print("输入有误，请进行合法输入\n")
def dec(s1):
    try:
        s1=s1.encode('utf-16')
        s1_code=base64.b64decode(s1)
        str(s1_code,encoding='utf-16')
        print("解密后的字符串为 ",s1_code,"\n")
    except:
        print("解密失败，请进行合法输入")
