class Solution:
   def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res, cur = [], []
        # candidates.sort()

        # def dfs(i, total):
        #     if total == target:
        #         res.append(cur[:])
        #         return
            
        #     if i == len(candidates) or total > target:
        #         return # back to og fn call

        #     # consider cand[i]
        #     cur.append(candidates[i])
        #     dfs(i + 1, total + candidates[i]) # discard num, but update the total

        #     # discard cand[i] and keep last saved total
        #     cur.pop() # backtrack condt

        #     while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
        #         i += 1

        #     dfs(i + 1, total) # keep old total while shifting i(discarding num)

        # dfs(0, 0)
        # return res


         cur, res = [], []
         candidates.sort()

         def dfs(i, total):
               if total == target:
                  res.append(cur[:])
                  return

               # lets define edge case
               if total > target or i >= len(candidates):
                  return

               # now we can consider cur number w/o repetition
               cur.append(candidates[i])
               # now recursive DFS
               dfs(i+1, total + candidates[i])

               # here after, we define the backtracking condt
               cur.pop()

               # now we check if the sorted array has repeated nums
               while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                  i += 1 # shift i

               # now again for recursive dfs, we consider next num and last total
               dfs(i + 1, total)

         dfs(0,0) # 1st fn call
         return res




