"""
Our goal is to reach the last idx -> len(nums) - 1

If we check from each idx, if we can reach goal, and discard if nums[i] == 0 -> cant jump from curr pos,
this will be costly -> exponential TC

So, we need to greedily check if we can reach goal
-> we can do this by maintaining farthest, and updating farthest as we iterate the array nums
We can identify deadlock we we come accross 0 -> here curr idx will be greater than farthest -> in this case we return False


"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        # init furthest
        furthest = 0
        for i in range(len(nums)):
            # check if we reached deadlock
            if i > furthest:
                return False
            # update furthest jump after curr iteration
            furthest = max(furthest, i + nums[i])
        
        return furthest >= goal