class stack():
    def __init__(self):
        self.ele=[]
    def push(self,new):
        self.ele.append(new)
    def pop(self):
        return self.ele.pop()
    def isempty(self):
        return self.ele==[]
    def peek(self):
        if not self.isempty():
            return self.ele[-1]
    def getstack(self):
        return self.ele
    def reverse(self):
            return self.ele.reverse()
            
s=stack()
print(s.isempty())
s.push("s")
s.push("w")
s.push("a")
s.push("t")
s.push("h")
s.push("i")
s.push("'s")
print(s.getstack())
s.pop()
print(s.isempty())

print(s.getstack())
print(s.peek())
s.reverse()
print(s.getstack())
