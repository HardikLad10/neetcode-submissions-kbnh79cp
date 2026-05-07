class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        nums.sort()


        def dfs(i):
            if i >= len(nums):
                res.append(cur[:])
                return

            
            # include cur num in subset
            cur.append(nums[i])
            dfs(i + 1)

            # discard cur num 
            cur.pop()

            # check if duplicate exists before recursive call
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res