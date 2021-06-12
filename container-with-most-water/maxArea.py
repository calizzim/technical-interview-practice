from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #define variables
        maxArea = 0 
        p1, p2 = 0, len(height)-1
        #main loop - while pointers are not on top of eachother
        while not p1 == p2:
            #update max area
            maxArea = max(maxArea, min(height[p1], height[p2])*(p2-p1))
            #move our pointers
            if height[p1] < height[p2]: p1 += 1
            else: p2 -= 1
        return maxArea

