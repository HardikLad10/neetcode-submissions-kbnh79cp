class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums

        heapq.heapify(nums)

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        return minHeap[0]