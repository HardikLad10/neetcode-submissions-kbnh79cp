"""
Brute force way of going to each cell(DFS) to check the main logic will cost us a TC of O(mn)^2 - which is too slow,
since there is a lot of repeated work.

So, lets flip the problem, and go from ocean to cell i.e.
pick cells from ocean borders( up, left for pacific, right and down for atlantic) -> and then go to each cell
The condition now will become height >= curr cell

In the code, we will maintain visit(atl and pac) sets -> that has cell positions, to make sure no duplicates are added using conditions.
atl and pac sets indicates if a cell can be reached from atl(up and left) and pac(right and down).

In our main function, we check our visit sets and compare them to atl and pac, and finally return co-ordinates of cell(append them in res list) that 
can be reached from both oceans(and vice versa).
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # lets init 2 sets for visit check
        atl, pac = set(), set()

        # our dfs fn

        def dfs(r, c, visit, prevHeight):
            # main logic check -> if cell in visit, if cell out of bound or if cell height < prev
            if ((r,c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                    return
            # if cond satisfies then add cell to visit
            visit.add((r, c)) # add co-ord pair to visit set
            # dfs on neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Now we run dfs from ocean to neighbor cells
        #For first and last ROW
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # first row
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c]) # last row

        # For first and last col
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # left col
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # right col

        res = [] # def res list
        # check on each cell
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r,c))

        return res        
