"""
We need to add the newInterval in a LOL of intervals
The newInterval can either be overlapping or it wont, sp 2 cases.

If the interval is non overlapping:
1. It can either be before the curr interval
2. Or it can be after the curr interval

Thus we will maintain a res list -> for each pass, we would append into this res list
for a for loop for fixed range(n) -> n = len(intervals array)
If else loop to determine if either newInterval is either before or after the curr interval i
Final else loop for the case of interval overlapping:
This will update the new interval to min(starting point of curr and newInt), max(end of curr int and newInt)

outside of the for loop, we append newInterval into res again -> this takes care of overlapping interval
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, n = [], len(intervals)

        for i in range(n):
            #Case 1 -> new interval before other intervals / curr interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # return res + other remaining intervals 
                return res + intervals[i: ]
            
            #Case 2 -> newInterval is after curr interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # since we dont know newInt position wrt other remaining intervals

            #Case 3 -> Overlap. In this case, merge and update into the newInterval
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])] 
            
        # Finally append newInterval in the result This takes care of elif and else cases
        res.append(newInterval)

        return res