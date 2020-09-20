from stack import stack #import previous file stack
s=stack()
num=int(input("enter"))
s=stack()
while(num>0):
    r=num%2
    s.push(r)
    num=num//2
s.reverse()        
print(s.getstack())
