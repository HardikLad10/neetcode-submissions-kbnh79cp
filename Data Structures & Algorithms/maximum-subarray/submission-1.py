"""
Given: nums array

Tf: a subarray(list of contiguous nums) that has the maxSum

we need to return maxSubarray(num)


So to think it through, this sounds like a sliding window problem

The goal is to adjust the window/subarray here
So we will iterate nums:
So a basic check is to see if our curr sum is +ve or not, if its -v2, we skip the prefix from 
our subarray and start from next val
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSub = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)

        return maxSub