for i in range(6):
    for j in range(i+1):
        print("*",end=" ")
    print("")

'''o/p:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * '''

for i in range(6,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("")

'''o/p:
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print("")
for i in range(6,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("")
'''o/p:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''
