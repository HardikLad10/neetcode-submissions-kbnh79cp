"""
In a given array nums -> find indices i and j such that nums[i] + nums[j] = target
target will always be given 

Also it is said that each input contains exactly one pair of i and j
So its safe to assume that input array cannot be empty

eg -> nums = [1, 3, 4, 6] target = 10
              0  1  2  3 
Thus out o/p array res = [2, 3]

explanation -> for i = 0, diff = target - 1 -> 9, see if there is 9 in nums.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], idx]
            seen[n] = idx # 1: 0

        
            