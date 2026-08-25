"""
Most - frequent
First lets think how to handle frequent?
better to have a hashmap of {val: freq}
Assume nums = [1, 1, 2, 2, 3], count = {1:2, 2:2, 3:1}
if k = 2, we want an output of [1,2]

Thus we need to have a bucket, where i is the freq, and freq[i] stores the val/ array of vals with that freq


"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # lets add val:freq to Hashmap
        for n in nums:
            # add count of curr val, if val repeats, update cnt
            count[n] = 1 + count.get(n, 0) # if n does not exits, count.get returns 0

        # lets init freq array -> array of arrays
        freq = [[] for _ in range(len(nums) + 1)]

        # !parse Hashmap, and add values in freq LOL
        # freq idx -> cnt, freq[idx] -> vals with that cnt
        for val, cnt in count.items():
            # eg, append [1, 2] at idx 2, 3 at idx 1 from out example
            freq[cnt].append(val)

        # a particular freq[idx] may have a list of nums, so we need to check that with given k
        # Run a desc for loop on fixed length -> dont want 0
        res = []
        max = len(freq) 
        for i in range(max - 1, 0, -1):
            # now parse indv list
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


            
        