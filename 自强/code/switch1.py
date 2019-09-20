def sw1(s1):
    dic=eval(s1)
    print(dic)
    #用,分解出单个元素
    pivot=re.compile(',+')
    cont=pivot.split(s1)
    for val in cont:
        #这部分是去掉两边的{ / }
        cont1=val.strip('{')
        cont1=cont1.strip('}')
        #以下是字典键值的分解
        pi2=re.compile(':')#用:拆分字典的键值
        unit=pi2.split(cont1)#unit应为两个元素组成的列表
        i=0
        element1=1
        element2=2
        for element_unit in unit:
            i=i+1
            a1=element_unit.count('\"')
            b1=element_unit.count('\'')
            if((a1==2) or (b1==2)):#如果是个字符串
                element_unit=element_unit.strip('\'')
                element_unit=element_unit.strip('\"')
                if(i==2):
                    str(element2)
                    element2=element_unit#直接赋过去
                    ans[element1]=element2
                else:
                    str(element1)
                    element1=element_unit
            elif((a1==0) and (b1==0)):#如果是个数
                a=eval(element_unit)
                if(i==2):
                    if(type(a)==int):
                        int(element2)
                    else:
                        float(element2)
                    element2=a
                    ans[element1]=element2
                else:
                    if(type(a)==int):
                        int(element1)
                    else:
                        float(element1)
                    element1=a
            else:
                raise(NameError)
