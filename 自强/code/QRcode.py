import sys
import qrcode
from PIL import Image
def qr():
    f=open('test.txt','r')
    fline=f.read()
    img=qrcode.make(fline)
    img.save('t.png')
    
    
