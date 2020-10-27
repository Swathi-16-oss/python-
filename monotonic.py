def monotonic(a):
    n=len(a)
    #if it is in ascending or desending order print true otherwise false
    return(all(a[i]<=a[i+1] for i in range(n-1)) or all(a[i]>=a[i+1] for i in range(n-1)))
a=list(map(int,input().split()))#to take multiple values as a input at a time by user
print(monotonic(a))

'''o/p:
1 4 6 7 8
True
>>> 
=============
4 1 7 2 9
False'''
