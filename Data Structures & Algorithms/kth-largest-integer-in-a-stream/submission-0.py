class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums # for current instance minHeap represents nums list
        heapq.heapify(self.minHeap) # heapify minHeap for curr instance
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # pops 1st ele i.e. smallest to maintain len = k
    def add(self, val: int) -> int:
        # this is the add fn, this return kth largest ele in curr stream

        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        
