class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[: ]) # append curr subset
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to discard nums[i]
            subset.pop() # backtrack condt
            dfs(i + 1) # recursive dfs call

        dfs(0)
        return res