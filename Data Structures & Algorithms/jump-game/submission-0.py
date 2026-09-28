"""
lastIdx = len(nums) - 1

Goal is to reach lastIdx

The greedy approach here, is to check if we can start from lastidx and reach first or no
because, the nums[i] is the max jumps that we can take, so it has to be always i + nums[i] >= goal

Thus, we init the array from 2nd last ele, and check logic and traverse back
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0