class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # init empty minHeap
        for x, y in points:
            dist = (x ** 2) + (y ** 2) # this is dist from origin(0,0)
            minHeap.append([dist, x, y]) # creates minHeap list of lists w (d,x,y)

        res = []
        heapq.heapify(minHeap) # by def sorts dist first

        while k > 0:
            dist, x, y = heapq.heappop(minHeap) # pops smallest set of (d,x,y)
            res.append([x,y])

            k -= 1

        return res