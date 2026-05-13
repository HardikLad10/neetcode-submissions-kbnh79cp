class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      # init empty arrays 
      res, cur = [], []
      # sort array
      nums.sort()
      # main fn only pass i
      def dfs(i):
         # get done with base fn
         if i >=len(nums):
            res.append(cur[:]) # append entire cur subset
            return

         # branch 1 - consider cur num and shift i
         cur.append(nums[i])
         dfs(i+1)

         # branch 2 - backtrack condt
         cur.pop()

         # check for duplicates
         while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

         # now branch 2
         dfs(i+1)

      dfs(0) # 1st fn call
      return res