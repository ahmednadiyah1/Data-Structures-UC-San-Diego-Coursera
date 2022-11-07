import sys

sys.setrecursionlimit(10**7)

class treeHeight:
    def __init__(self):
        self.num=int(input())
        self.parents=list(map(int, input().split()))


    def get_height(self):
        depth=[0]*self.num
        for i in range(len(self.parents)):
            n=self.parents[i]
            depth[i]=self.get_depth(n)
        return max(depth)

    def get_depth(self,n):
        if n==-1:
            return 1

        m=self.parents[n]
        height=1+self.get_depth(m)
        return height

h=treeHeight()
print(h.get_height())




