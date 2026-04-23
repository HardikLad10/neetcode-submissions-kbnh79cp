class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #since we cant make maxHeap ideally, we make all vals -ve
        # so that they -ve(largest) is at index 0 always and so on

        stones = [-s for s in stones] # O(n)
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # -ve(largest)
            second = heapq.heappop(stones) # new -ve(largest)
            if second > first:
                # push diff only if one greater than other, else pop both(same)
                heapq.heappush(stones, first - second) # -ve(largest - 2nd largest)

        stones.append(0) # for edge case, if stones list empty, return 0
        return abs(stones[0])
