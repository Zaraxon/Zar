from code.QRcode import *
from code.switch import *
from code.coding import *
print("*-----------------------------------*\n")
print("|*这是一个功能不完善的小工具箱*|\n")
print("*-----------------------------------*\n")


def select1():
    select_code = input("请选择加密(e)/解密(d)\n")
    if(select_code == 'e'):
        Encoding(input("请输入待加密字符串 "))
    elif(select_code == 'd'):
        Decoding(input("请输入待解密字符串 "))
    else:
        print("输入有误！")
    re_code = input(">>是否进行下一次加/解密？（Y/N）<<")
    if(re_code == 'Y'):
        select1()


def select2():
    Switch(input("请输入字典\n"))


def select3():
    QR_code(input('请输入要转化的数据'))


def app():
    print("**请输入工具前序号以使用工具**\n\n")
    select = 1
    select = eval(
        input("*1.字符串加/解密（无法正确解密中文）*\n*2.字典反转*\n*3.将输入数据生成QR code（生成文件为trans.png）*\n"))
    if(select == 1):
        select1()
    if(select == 2):
        select2()
    if(select == 3):
        select3()
    re_app = input("\n\n再次使用工具箱？（Y/N）")
    if(re_app == 'Y'):
        app()


app()
