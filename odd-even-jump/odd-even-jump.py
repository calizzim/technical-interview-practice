import bisect
class NumI:
    def __init__(self,val,index):
        self.val = val
        self.index = index
    def __lt__(self, other):
        return self.val < other.val
    def __str__(self):
        return str([self.val,self.index])

class Solution:
    def oddEvenJumps(self, arr):
        canReach = [[False,False] for i in range(len(arr))]; canReach[-1]=[True,True]
        tracker = [NumI(arr[-1],len(arr)-1)]
        for index in range(len(arr)-2,-1,-1):
            #check if we can reach the end if odd
            gotoIndex = bisect.bisect_left(tracker,NumI(arr[index],0))
            if gotoIndex != len(tracker):
                gotoIndex = tracker[gotoIndex].index
                if(canReach[gotoIndex][1]):
                    canReach[index][0] = True
            #check if we can reach the end if even
            gotoIndex = bisect.bisect_left(tracker,NumI(arr[index],0))
            if gotoIndex == len(tracker) or tracker[gotoIndex].val != arr[index]: gotoIndex -= 1
            if gotoIndex != -1:
                gotoIndex = tracker[bisect.bisect_left(tracker,NumI(tracker[gotoIndex].val,0))].index
                if(canReach[gotoIndex][0]):
                    canReach[index][1] = True
            #add current value to list to be tracked
            bisect.insort_left(tracker,NumI(arr[index],index))
        print(canReach)
        return len(list(filter(lambda e: e[0], canReach)))

s = Solution()
print(s.oddEvenJumps([10,13,12,14,15]))
