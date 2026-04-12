class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # key is num, val is i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i] # returns index of the diff, and the index of the current num
            prevmap[n] = i   # gives key val pairing [2,1,3,5] Gives 2:0
