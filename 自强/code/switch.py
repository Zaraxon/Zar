import json
def Switch(s1):
    ans=eval(s1)
    print('Json字符串为：',json.dumps(ans),'\n')
    print('类型为',type(json.dumps(ans)),'\n')
    try:
        ans_turn={}
        for x,y in ans.items():
            if(y not in ans_turn):
                ans_turn[y]=x
                continue
            if(type(ans_turn[y])!=list):
                tem=[]
                tem.append(x)
                tem.append(ans_turn[y])
                ans_turn[y]=tem
            else:
                ans_turn[y].append(x)
        print('反转后的字典为：',ans_turn,'\n')
        print('类型为',type(ans_turn))
    except:
        print("您输入的值中可能包含列表/字典/元组，由于要翻转，这些输入是不合法的，请重新输入")
            
        
                    
            
        
        
            
        
            
            
           

    
    
    

       
       
