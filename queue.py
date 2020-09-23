class queue:
    def __init__(self):
        self.item=list()
    def push(self,new):
        self.item.append(new)
    def pop(self):
        if len(self.item)>0:
            return self.item.pop(0)
        else:
            return None
    def peek(self):
        if len(self.item)>0:
            return self.item[-1]
        else:
            return None
    def getsqueue(self):
        return str(self.item)
q=queue()
q.push('D')
q.push('s')
q.push('w')
q.push('a')
q.push('t')
q.push('h')
q.push('i')
q.push('.')
print(q.getsqueue())
q.pop()
print(q.getsqueue())
