"""
Given that intervals is sorted and nonOverlapping -> res should also be the same -> i.e. no [[1,2][2,4]] -> this is an overlap

So we want to fit the newInterval in all the intervals, and make sure that the res is sorted and without overlaps

Lets take this eg -> intervals = [[1,2],[3,5],[9,10]], newInterval = [5,7] -> o/p should be [[1,2],[3,7],[9,10]]

The brute force approach is to simply add both intervals and newI in the res, and then sort-> O(nlogn)
But this will still have overlaps

Thus we can div this prob in 3 phases
p1 -> add intervals before startTime of newInterval in res
p2 -> while intervals that do not start after newInterval endTime, merge and add[checking min start and maxEnd] to res
p3 -> Add all the *remaining* intervals to the res 
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # init res and index
        res, i = [], 0
        n = len(intervals)
        # Phase 1 -> add intervals in res that *strictly* end before newI startTime
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Phase 2 -> Merge with newInterval and add to res
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update min start and max end Time
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # append the updated newInterval in the res
        res.append(newInterval)

        # Phase 3 -> use index and append all remaining intervals to res
        for j in range(i, n):
            res.append(intervals[j])

        return res