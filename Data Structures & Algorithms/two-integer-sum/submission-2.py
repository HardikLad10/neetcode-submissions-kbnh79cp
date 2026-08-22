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
        seen = {} # val: idx

        # iterate nums
        for i, val in enumerate(nums):
            # calc difference
            diff = target - val #here val is curr val at i
            if diff in seen:
                return [seen[diff], i] # happy flow, returns idx of diff and i in a list
            seen[val] = i # if the diff is not in the hashmap, add the curr val: idx pair
        