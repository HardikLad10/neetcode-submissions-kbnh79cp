"""

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0]) 

        # def our dfs fn( capture )

        def capture(r, c):
            # main condition
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
                or board[r][c] != 'O'):
                return
            
            # do the swap
            board[r][c] = 'T'
            # propagate to neighboring cells to check if 'O' exits, if it does, swap to T -> cant capture
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)


        # part 1. traverse grid, swap O -> T

        for r in range(ROWS): 
                for c in range(COLS):
                    if ( board[r][c] == 'O' and
                        r in [0, ROWS - 1] or c in [0, COLS - 1]):
                        capture(r, c)

        # part 2. Traverse, swap 0 -> X and T -> O

        for r in range(ROWS): 
                for c in range(COLS):
                    if board[r][c] == 'O':
                        board[r][c] = 'X'
                    elif board[r][c] == 'T':
                        board[r][c] = 'O'

