for i in range(5):
    print("") #to print new line
    
    for j in range(5):
        print(i+1,end="")#end to print new line
'''o/p
    11111
    22222
    33333
    44444
    55555'''

for i in range(5):#for rows
    print("")
    for j in range(i+1):
        print(j+1,end="")#for numbers
 
''' o/p
    1
    12
    123
    1234
    12345'''
  
for i in range(5):#for rows
    print("")
    for j in range(i+1):
        j=i
        print(j+1,end="")#for numbers
'''o/p
1
22
333
4444
55555'''

for i in range(5,0,-1):
    print("")
    for j in range(1,i+1):
        print(j,end="")
'''o/p
12345
1234
123
12
1'''
