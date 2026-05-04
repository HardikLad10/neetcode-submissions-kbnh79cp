class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #since we cant make maxHeap ideally, we make all vals -ve
        # so that they -ve(largest) is at index 0 always and so on


        stones = [-s for s in stones] # appending same -ve vals in array
        heapq.heapify(stones) # now vals are arranged in -(max1), -(max2)...

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # now we have -(max1) and -(max2) with us, we just need to check condt
            # in reverse logic
            if second > first:
                heapq.heappush(stones, first - second) # this again gives us the desired -val

        stones.append(0) # to get rid of edge case for null array

        return abs(stones[0])
