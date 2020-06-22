print("*-----------------------------------*\n")
print("|*这是一个功能不完善的小工具箱*|\n")
print("*-----------------------------------*\n")
from code.coding import *
from code.switch import *
from code.QRcode import *
def sel1():
    j=input("请选择加密(e)/解密(d)\n")
    if(j=='e'):
        ec(input("请输入待加密字符串 "))
    elif(j=='d'):
        dec(input("请输入待解密字符串 "))
    else:
        print("输入有误！")
    c=input(">>是否进行下一次加/解密？（Y/N）<<")
    if(c=='Y'):
        sel1()
        
def sel2():
    try:
        Switch(input("请输入字典\n"))
    except:
        print("您进行了非法输入，请按正确格式输入字典\n")
def sel3():
        qr()
def app ():
    print("**请输入工具前序号以使用工具**\n\n")
    sel=1
    sel=eval(input("*1.字符串加/解密（无法正确解密中文）*\n*2.字典反转*\n*3.将.txt文件生成QR code（使用前将要转化的数据写入test.txt，生成文件为t.png）*\n"))
    if(sel==1):
        sel1()
    if(sel==2):
        sel2()
    if(sel==3):
        sel3()
    C=input("\n\n再次使用工具箱？（Y/N）")
    if(C=='Y'):
        app()

app()
