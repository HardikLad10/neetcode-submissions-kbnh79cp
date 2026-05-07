class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closedN, cur):
            # define base fn first
            if openN == closedN == n:
                res.append(cur)
                return
            
            # now for the 1st case - add '('
            if openN < n:
                # do a recursive fn call and append '(' to cur string
                backtrack(openN + 1, closedN, cur + '(') # also inc openN
            
            # now 2nd case - add ')'
            if closedN < openN:
                # again recursive call while appending to cur
                backtrack(openN, closedN + 1, cur + ')')

        # 1st fn call, pass empty string in place of curr
        backtrack(0, 0, "")    
        return res
