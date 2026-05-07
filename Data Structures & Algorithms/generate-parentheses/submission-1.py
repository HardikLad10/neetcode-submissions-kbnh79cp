class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closeN, cur):
            if openN == closeN == n:
                res.append(cur)  # just append directly, no join needed
                return

            if openN < n:
                dfs(openN + 1, closeN, cur + "(")

            if closeN < openN:
                dfs(openN, closeN + 1, cur + ")")   

        
        dfs(0, 0, "")
        return res