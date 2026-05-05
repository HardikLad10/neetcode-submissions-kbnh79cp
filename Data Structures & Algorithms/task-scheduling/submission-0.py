class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # hashmap of counts of each task -> "A": 4, "B":2
        maxHeap = [-cnt for cnt in count.values()] #-num for all values in hashmap
        heapq.heapify(maxHeap) # creates a maxHeap

        # init time var
        time = 0
        # idletime is the time at which the task can be added to heap again
        q = deque() # doub ended with [-cnt, idletime]
        while q or maxHeap: 
            time += 1 # increment time first
            if maxHeap: # if curr maxHeap not null  
                cnt = 1 + heapq.heappop(maxHeap) # dec count of occurance
                # add to deque if its !0, can be added after idletime
                if cnt:
                    q.append([cnt, time + n])
                
            # if deque non empty and idetime achieved,     
            if q and q[0][1] == time:
                # pop from deque and add only cnt to heap
                heapq.heappush(maxHeap, q.popleft()[0])


        return time