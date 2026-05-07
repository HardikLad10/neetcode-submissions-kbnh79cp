class Solution:
    """ We will try to solve this problem in the most brute force way possibe
        i.e. start from board[0][0], and check all directions for word[i] and 
        return true or false depending if we find it in contiguous traversal or not."""
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0]) # finding value for m and n in board

        # rather than updating the path as a set, lets just mark it as well traverse the matrix

        # dfs fn init

        def dfs(r, c, i): 
            # base fn
            if i == len(word): return True 

            # null condt
            # this takes care of out of bound, and wrong char
            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return False
            # now wrong char
            if board[r][c] != word[i]:
                return False

            temp = board[r][c] # storing matched char in temp var
            board[r][c] = '#'   # marking path 

            found = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1) )

            # backtrack condition
            board[r][c] = temp

            # return the result
            return found # either True or False

        
        # try every cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): 
                    return True

        return False