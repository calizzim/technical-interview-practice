from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [0]
        nums.sort()
        for index, num in enumerate(nums):
            if index and nums[index]==nums[index-1]: continue
            target = -num; other = nums[index+1:]
            h = dict()
            for n in other:
                if n in h: h[n]+=1
                else: h[n] = 1
            for n in other:
                h[n]-=1
                if target-n in h and h[target-n]:
                    if ans[-1] != [num,n,target-n]: ans.append([num,n,target-n])
        return ans[1:]

s = Solution()