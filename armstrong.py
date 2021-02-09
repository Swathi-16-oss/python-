list=[]
list1=[]
total=0
b=0
n=int(input("enter number of digits"))
for i in range(1,n+1):
    ele=int(input("enter the digit"))
    list1.append(ele)
    a=(ele**n)
    list.append(a)
for j in range(0,len(list)):
               total=total+list[j]
b=int(''.join(str(k) for k in list1))
if(b==total):
    print(b,"is armstrong")
else:
    print(b,"is not armstrong")

    
'''o/p:
enter number of digits3
enter the digit4
enter the digit0
enter the digit4
404 is not armstrong
>>>>>>>>>>> 
enter number of digits3
enter the digit4
enter the digit0
enter the digit7
407 is armstrong
'''
