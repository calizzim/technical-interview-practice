from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for num in nums:
            if num in d: d[num] += 1
            else: d[num] = 1

        for num in nums:
            d[num] -= 1
            needed = target - num
            if needed in d and d[needed]>0:
                if(num==needed):
                    first = nums.index(num)
                    nums.pop(first)
                    second = nums.index(num) + 1
                    return [first, second]
                return [nums.index(needed),nums.index(num)]
