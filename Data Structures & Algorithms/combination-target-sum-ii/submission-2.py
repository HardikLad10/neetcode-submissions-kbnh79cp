class Solution:
   def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return
            
            if i >= len(candidates) or total > target:
                return # back to og fn call

            # consider cand[i]
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i]) # discard num, but update the total

            # discard cand[i] and keep last saved total
            cur.pop() # backtrack condt

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i + 1, total) # keep old total while shifting i(discarding num)

        dfs(0, 0)
        return res