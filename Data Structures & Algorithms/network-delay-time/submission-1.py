"""
Given data:
times is a list of list
n = num of nodes
times = [[ui, vi, ti], [u2,v2,t2]]
Also given k(1 to n) -> indicates from which node to start

Can make a bfs() -> pass prevTime as a param in the fn

Since we want to get the min time it takes for all nodes to receive signal, we can use minHeap(//r to Djikstra)
we add adjacent nodes to minheap, nodes with the shortest dist will be popped first
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # if k > n:
        #     return -1
        
        # create a hashmap of all the nodes edges -> {u: (v, w)} -> w is the time to reach v from u

        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # init minHeap on k

        minHeap = [(0, k)] # k is the node and 0 is the time(init time)
        t = 0 # this is the time that we will return at end of problem
        visit = set()

        # run a while loop to empty the minHeap
        while minHeap:
            w1, n1 = heapq.heappop(minHeap) # we pop the node with the least weight
            # check if node present in visit set
            if n1 in visit:
                continue
            #alt logic
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1

