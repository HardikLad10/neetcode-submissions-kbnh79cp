"""
heights[i] is the height
We may choose any 2 bars to form a container -> i.e we have to return area of the container -> compare with last max

We take l,r = 0, len(heights) - 1
Run a while loop l<r:
calc area
check res = max(area, res)

take 
edge cases:
if height = 0
if all heights are same

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
