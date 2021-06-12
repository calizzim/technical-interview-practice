import bisect
class NumI:
    def __init__(self,val,index):
        self.val = val
        self.index = index
    def __lt__(self, other):
        return self.val < other.val
    def __str__(self):
        return str([self.val,self.index])

l = [1,2,3,4,5]
m = l[0:2]
print(m)
l[0] = 2
print(m)