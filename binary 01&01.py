n=int(input("enter number"))
a=[]
while(n>0):
    r=n%2
    a.append(r)
    n=n//2
s=str(''.join(str(i) for i in a))
bin=s[::-1]
print(bin)
#for 10 it take 010(exception)
if(len(bin)==2 and bin.find("10")>-1):
    print("yes")
elif bin.find("01")>-1 and bin.find("10")>-1:
    print("yes")
else:
    print("no")

    
'''o/p:
enter number4
100
no
>>> 
enter number5
101
yes
>>> 
================
enter number2
10
yes
>>> 
==================
enter number3
11
no
==== ==========
enter number4
100
no'''
