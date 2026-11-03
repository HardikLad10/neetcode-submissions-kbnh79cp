"""
We need to find min Intervals that we can remove to make rest non overlapping -> i.e. Max no of non overlapping intervals

How to choose what to remove? -> if nextI overlaps with currI -> remove
e.g. [[2,5],[4,6]] -> remove [4,6]

Now, its imperative to sort intervals -> given array not sorted
Since we will greedily choose first interval after sorting, its better to sort by end time and not start time

*choosing intervals that finish earlier leaves more space for future meetings*
e.g [[1,10][2,3][3,5]] -> better to sort by end time and not start time

so we maintain count -> return len(intervals) - cnt -> this gives how many to remove
also maintain endI --> end of currI
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        #Since not given that intervals always have something
        if not intervals:
            return 0

        #sort by end time
        intervals.sort(key = lambda x:x[1])

        # init end of currI(first after sort) and counter(1 since we greedily add the first)
        cnt, endI = 1, intervals[0][1]

        # interate from next till end of List
        for i in range(1, len(intervals)):
            #check logic -> qualifying intervals
            if intervals[i][0] >= endI:
                #update endI and cnt
                endI = intervals[i][1]
                cnt += 1
        
        # now return intervals that need removal -> len(intervals) - qualifying intervals cnt
        return len(intervals) - cnt

        