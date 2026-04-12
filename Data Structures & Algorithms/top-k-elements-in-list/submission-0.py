class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap
        freq = [[] for i in range(len(nums) + 1)] # freq bucket that stores list of lists and has index 0-n hence +1

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Common step to init k,v in hashmap. We are assigning n:count here 
        for n,c in count.items():   # .items gives us the k,v pairs
            freq[c].append(n) # most imp step in making the buckets. freq is a list of lists. i of outer list is the count, element(lists) in freq list are the nums with count = i

        res = []
        for i in range(len(freq) - 1, 0, -1):  # traversing in desc order
            for n in freq[i]:  
                res.append(n)
                if len(res) == k: 
                    return res



