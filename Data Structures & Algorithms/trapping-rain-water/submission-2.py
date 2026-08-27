"""
We need to visualize this
if height = [0, 1, 0, 2, 0, 3]
we can store water at i =2(1), and i = 4(2) 

This means we can store water = min(leftmax, rightmax) - height[i]
so we compare curr height with leftmax and rightmax in every pass, update as such, and 
check the above condition
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        # init max heights to edge vals
        leftMax, rightMax = height[l], height[r]
        water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                water += leftMax - height[l]

            else:
                r -=1
                rightMax = max(height[r], rightMax)
                water += rightMax - height[r] # water either 0 if rMax = curr height, or diff

        return water