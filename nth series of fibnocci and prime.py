'''fib and prime
1 2 1 3 2 5 3 7 5 11 8 13 13 17

fib=1 1 2 3 5  8  13
 n =1 3 5 7 9  11 13 (n//2+1)

 
pri=2 3 5 7 11 13 17
 n= 2 4 6 8 10 12 14 (n/2)'''




def prime( n):
    i=0
    k=1
    while(i<n):
        if isprime(k):
            i=i+1
        k=k+1
    return k-1
def isprime(n):
    if(n<2):
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def fibnocci(n ):
    fib=[0]*(n+1)
    fib[1]=1
    for i in range(2,n+1,1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]
def f(num):
    if(num%2==0):
        return prime(num//2)
    else:
        return fibnocci((num//2)+1)

num = int(input("enter a number"))
print(f(num))

'''o/p:
enter a number11
8
enter a number13
13'''
