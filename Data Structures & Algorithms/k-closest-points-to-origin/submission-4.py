class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return None
        # init minHeap (empty)
        minHeap = []

        # now calc dist for each pair of co-ords of pts in the inp array
        for x,y in points:
            dist = x**2 + y**2 # since x2,y2 is 0, dist is easy to calc
            minHeap.append([dist, x, y]) # append minHeap LoL w dist frm O and its co-ords

        # now we heapify the minHeap
        heapq.heapify(minHeap)
        #init res array
        res = []
        # now that we have our minHeap ready, we just pop the top k pairs that satisfy our condt
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            
            # store only co-ords in res, thats what we need to return
            res.append([x, y])
            k -= 1 # dec k

        return res