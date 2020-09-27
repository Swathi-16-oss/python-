for i in range(6):
    print("")
    for i in range(0,i,1):
        print(2**i, end=' ')
'''o/p
1 
1 2 
1 2 4 
1 2 4 8 
1 2 4 8 16'''

for i in range(6):
    print("")
    for i in range(0,i,1):
        print(2**i, end=' ')
    for i in range(i-1,-1,-1):
        print(2**i,end=" ")

'''o/p
1 
1 2 1 
1 2 4 2 1 
1 2 4 8 4 2 1 
1 2 4 8 16 8 4 2 1 '''
