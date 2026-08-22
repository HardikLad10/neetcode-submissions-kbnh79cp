"""
nums = [5, 3 , 1, 2] target = i + j
        0  1   2  3
We are given that the array nums has exactly one pair [] ie i, j which makes the targetSum

since index is also needed, we iterate thru enumerate, 
and maintain a HASHMAP, which stores nums[i]: i as k, v
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initiate a seen Hashmap
        seen = {}
        
        # iterate thru nums to get i, val pair
        for i, value in enumerate(nums):
            diff = target - value # value is the current val
            if diff in seen:
                return [seen[diff], i] # returns pair of indices
            seen[value] = i
        

            

        