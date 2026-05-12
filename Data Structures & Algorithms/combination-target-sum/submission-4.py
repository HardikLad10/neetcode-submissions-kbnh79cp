class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return
            
            if i >= len(candidates) or total > target:
                return # back to og fn call

            # consider same num
            cur.append(candidates[i])
            dfs(i, total + candidates[i]) # we keep same num, but update the total

            # discard curr num(i + 1) and keep last saved total
            cur.pop() # backtrack condt
            dfs(i + 1, total) # keep old total while shifting i(discarding num)

        dfs(0, 0)
        return res
