"""
Given intervals may or may not be sorted. 
Since we want to return non overlapping && mergedIntervals -> we need to sort by startTime here.

We can maintain a merged[], and parse the intervals array and append non overlapping intervals into merged.

How to check overlap? 
-> is currInterval[0] > merged_prev[1] -> add to merge
-> also check if currInterval already exist in the set
-> else replace merged prev endTime with max(currI[1], merged_prev[1])

return mergedArray
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we sort by startTime
        intervals.sort(key = lambda x:x[0])
        merged = []

        for interval in intervals:
            # check if currI exist in set or if currI startTime does not overlap
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
            
        return merged