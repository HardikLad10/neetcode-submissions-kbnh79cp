"""
Given array nums, and an integer k -> we need to return a list[] containing top k freq elements

eg, if nums = [1,2,2,3,3,3], k = 2 -> we should return [3,2] in any order

count = {1:1, 2:2, 3:3}
Now we make a freq bucket array -> where i is the freq and freq[i] is a list of nums that occur i times from the input
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # count = {1:1, 2:2, 3:3}

        freq = [[] for _ in range(len(nums) + 1)]


        res = []
        for val, occr in count.items():
            freq[occr].append(val)

        for n in range(len(freq) - 1, 0, -1):
            for num in freq[n]:
                res.append(num)
                if len(res) == k:
                    return res


        