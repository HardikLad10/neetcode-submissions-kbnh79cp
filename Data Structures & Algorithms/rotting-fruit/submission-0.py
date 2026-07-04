"""
The idea here is, rotten orange(s) make adjacent oranges rotten as well, for each unit of time.

Logically, we have to take note of all rotten oranges, and append their positions in a deque.
In the same loop/iterations, we also need to check how many fresh oranges we have, and increment the fresh counter

Now, since we (may) have multiple rotten oranges, it is imperative to run BFS, on all adjacent cells or each rotten orange..
and check if the cell is either:
0 - nothing
1 - fresh -> then turn it rotten, i.e. 2
2 - dont do anything ?
check the edge cases while running the bfs for adjacent cells here

Then we inc time.

Finally we return the time taken to rot all oranges, if there is no fresh orange left. If there is, we return -1
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        # len of rows and cols in the grid for n X m
        ROWS, COLS = len(grid), len(grid[0])

        # Check all rotten and fresh oranges in the grid

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        # directions list
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Now we run BFS on each adjacent cell of rotten orange
        
        while q and fresh > 0:
            # This for loop insures that we run multi source BFS. i.e. run on each rotten orange for curr iteration
            for i in range(len(q)):
                r, c = q.popleft() # pop first rc pair from queue
                # Now we will check for all neighbors
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    # Check bounds, and turn rotten if fresh
                    # This condition will skip rotten fruits and empty cells
                    if (row < 0 or row == ROWS or 
                        col < 0 or col == COLS or
                        grid[row][col]!= 1):
                        continue
                    # Rot an orange    
                    grid[row][col] = 2
                    q.append([row, col]) # append r, c location in deque
                    # dec fresh fruit cnt
                    fresh -=1
            time += 1
        
        return time if fresh == 0 else -1


          