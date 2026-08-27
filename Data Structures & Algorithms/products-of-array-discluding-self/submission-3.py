"""
say nums = [1, 2, 3, 4]
res = [24, 12, 8, 6]
prod = 0
lets iterate for num in nums:
then j in nums:
if j == num
continue
else
prod += num*j

res.append prod
return prod
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # makes res array of size n-1 [1, 1, 1, 1]
        res = [1] * n

        #prefix sum/prod
        pref = 1
        for i in range(n):
            # load prefix into the result
            res[i] = pref
            # now build pref -> curr val* prev val
            pref *= nums[i]

        post = 1
        # we calc post from end -> start
        for i in range(n - 1, -1, -1):
            # load postfix and last calculated pref into final res
            res[i] *= post
            # calc curr postfix
            post *= nums[i] 
    
        return res