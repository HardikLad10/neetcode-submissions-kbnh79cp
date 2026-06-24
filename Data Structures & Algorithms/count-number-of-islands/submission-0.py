"""
What we are doing here is always checking if curr pos is 1, if not, 
dont bother. 
If it is 1, we check if its in visited, if not, we append island counter.

We will be doing iterative BFS on this grid to update our visited set and,
ULTIMATELY, RETURN OUR ISLAND COUNTER
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        rows, cols = len(grid), len(grid[0]) # gives us the len of r and c
        visit = set()
        islands = 0 # init ctr

        # bfs function (iterative)
        def bfs(r, c):
            # init deque
            q = collections.deque()
            visit.add((r,c)) # add curr r,c comb as tuple in visit set
            q.append((r,c))

            while q:
                row, col = q.popleft() #pop the position tuple from deque
                # init directions, i.e. r, l, up and down
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                # now compute for every directional r and c from curr pos
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        visit.add((r, c))
                        q.append((r,c))


        
        # check for curr val
        for r in range(rows):
            for c in range(cols):
               if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


