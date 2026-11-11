"""We are given that there is always a valid answer, thus no need to check that edge case -> this tells us that max_reach will not overflow

Intuition is that if we check each idx, and consider each jump, we can get to the min(jump) -> but as values inc, the checks grow exponentially

thus, we need to do minimal checks and make sure we reach to the min(jumps) req to reach end. What is end -> len(nums)

Each nums[i] give us the farthest reach from that i -> i+ nums[i] -> curr farthest reach
Thus we need to check the max_farthest_reach -> this gives us the levels from each farthest reach. e.g.
Input: nums = [2,1,2,1,0]
        lvl    0 1 1 2 2

For the check, we can maintain farthest_reach, current_end, jump_counter"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        
        farthest_reach = 0
        jump_counter = 0
        current_end = 0 #current level end 

        # since our goal is len(nums), we can skip that iteration
        for i in range(len(nums) - 1):
            # check curr farthest reach
            farthest_reach = max(farthest_reach, i + nums[i])

            if i == current_end:
                jump_counter += 1
                current_end = farthest_reach
        
        return jump_counter
