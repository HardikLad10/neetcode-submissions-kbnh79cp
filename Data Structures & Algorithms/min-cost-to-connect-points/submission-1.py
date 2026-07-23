"""
Cost to connect point a(xi, yi) and b(xj, yj) is |xi - xj| + |yi - yj|
We need the min cost to connect all pts together, such that there is only one path.

Since we only have pt co-ordinates and no edges, we have 2 parts in this problem:
1. Create (all) from a pair(xi, yi)
2. Apply Prim's algo to fin min dist/cost for the optimal solution and to create a single path

tc is O(n^2logn) -> n^2 for adjacency list + n^2*log n to add to minHeap and retrieve 
mincost node from minHeap

Explanation:
from points[[x1, y1], [x2, y2], ...] -> we take n = len(points)
and then assume all points from 0 to n-1, i.e. point0, point1, ....
because we need dist from point0 to all points and so on....
so for the adj list, we will store 
adj = {pointi: list of [[cost1, point1], [cost2,point2]]}


"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Make adjacency list {pointi: list of [[cost1, point1], [cost2,point2]]}
        adj = {i:[] for i in range(n)}
        # adding pts to adjList
        for i in range(n):
            x1, y1 = points[i]
            # now to get dist from points[i] to others
            for j in range(i + 1, n):
                x2, y2 = points[j]
                #manhattan dist
                dist = abs(x1 - x2) + abs(y1 - y2)
                #now store this pair in adjList
                adj[i].append([dist, j])
                adj[j].append([dist, i])


        # Prims algo logic
        res = 0
        visited = set()
        # Init minHeap with [cost, point]
        minHeap = [[0, 0]]

        while len(visited) < n: 
            cost, i = heapq.heappop(minHeap)
            # skip iteration if curr pt already visited, i.e. mindist calculated
            if i in visited:
                continue
            # inc res with curr cost -> gives us the latest minCost of the path
            res += cost
            visited.add(i)
            # CRIT! 
            # now we check all adj neighbors to curr pt i
            # then add all unvisited neighbors to our minHeap
            # the cost that we add will be relative to i not point0
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res


