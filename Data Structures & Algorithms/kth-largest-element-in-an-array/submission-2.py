class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We will maintain a heap of size k for this question
        # Lets iterate through nums, and push each num in heap
        minHeap = [] # lets name it minheap to avoid confusion
        for num in nums:
            heapq.heappush(minHeap, num) # append curr num in heap

            # Now we check if our minHeap size exceeds k, if so, then pop smallest
            if len(minHeap) > k:
                heapq.heappop(minHeap) 

        # in this way, we store only k largest elements in the Heap and returning kth largest
        return minHeap[0]