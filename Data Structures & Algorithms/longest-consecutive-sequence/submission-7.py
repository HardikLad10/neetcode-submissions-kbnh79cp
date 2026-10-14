"""
eg nums = [0,4,4,1,2,3] -> longest = 5

Some assumptions about the problem:
1. Array is not sorted
2. Array may contain dup

The first thing comes to the mind is that -> we can sort the array, 
run a for loop and update longest until num[i+1] = nums[i] + 1

but sorting takes O(nlogn) time

a better way would be to maintain a hashset to check if next num exists in the set or not -> O(1) lookup

take the same example, we convert nums to set -> dedup done
numSet = {0, 4, 1, 2 ,3}

now for our longest, we first need to know where to start -> thus we check if num - 1 not in set
-> start is at 0, once we have this, we can run a while loop until num + 1 in set: update longest

then finally return longest
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                locallongest = 0
                while num + locallongest in numSet:
                    locallongest += 1
            
                longest = max(longest, locallongest)

        return longest