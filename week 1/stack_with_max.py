class stack:

    def __init__(self):
        self.stack=[]
        self.auxstack=[]

    def push(self,n):
        if (self.auxstack):
            if self.auxstack[len(self.auxstack)-1]<=n:
                self.auxstack.append(n)
            else: self.auxstack.append(self.auxstack[len(self.auxstack)-1])
        else: self.auxstack.append(n)
        self.stack.append(n)

    def pop(self):
        assert(self.stack)
        assert(self.auxstack)
        self.stack.pop(len(self.stack)-1)
        self.auxstack.pop(len(self.auxstack)-1)

    def max(self):
        assert(self.auxstack)
        return self.auxstack[len(self.auxstack)-1]


Stack=stack()
num_queries=int(input())
for i in range(num_queries):
    query=input().split()
    if query[0]=="push":
        Stack.push(int(query[1]))

    elif query[0]=="pop":
        Stack.pop()
    elif query[0]=="max":
        print(Stack.max())
    else:
        assert(0)




