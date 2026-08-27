"""
Given:
that the elements do not have to be consecutive in og array -> can we sort array?
eg nums = [3, 0, 4, 1, 5, 20]
nums.sort() -> [0, 1, 3, 4, 5 ,20]
so if we iterate this, and have a check var that has the longest seq, we can return that check 
at the end, and call it a day

To check consecutive seq -> we simply check if nums[i] == nums[i - 1] + 1 -> check += 1
Edge cases:
Empty array? -> return None?


Optimal soln
Sort takes nlogn, what if we can skip that?

Lets make the given array nums -> set(nums) -> this given us O(1) retrieval 

Thus we can check if our prev is in set, if yes we update the cnt
Then we inc the cnt until next is in set...
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        # init longest
        longest = 0
        # now we iterate the set
        for num in numSet:
            # we check for start of series
            if (num - 1) not in numSet:
                # Then we reset local longest 
                localLongest = 0
                while num + localLongest in numSet:
                    localLongest += 1
                longest = max(longest, localLongest)
        return longest
                    


        