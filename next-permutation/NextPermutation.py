from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #edge cases
        if len(nums) < 2: return
        #find first in decending order in the reverse direction
        current = len(nums) - 2 
        while current != -1 and nums[current] >= nums[current + 1]: current -= 1
        if current != -1:
            #swap this with the least of the values greater than it (find one less then go one before that)
            swap = current + 1
            while swap != len(nums)-1 and nums[swap+1] > nums[current]: swap += 1
            nums[current], nums[swap] = nums[swap], nums[current]
        #reverse the order of the numbers greater than it
        current += 1; swap = len(nums) - 1
        while current < swap:
            nums[current], nums[swap] = nums[swap], nums[current]
            current += 1; swap -= 1
        print(nums)
s = Solution()
s.nextPermutation([5,1,1])