"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
So intervals will have pairs of [start, end], each pair being one interval

eg intervals = [(5,8),(9,15)] -> (5,8) is one interval, 5 being start time 8 being end time

We want to check if a person could attend all meetings -> true if possible false if cant

v simple logic to determine -> we first need to sort by start time, so we know that we are checking 
intervals chronologically

Now if end time of curr interval > start time of next interval -> there is an overlap -> return false

else return true
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        # Sort by start time
        intervals.sort(key = lambda x: x.start)

        # Iterate the LOL chrono
        for i in range(len(intervals) - 1):
            currI = intervals[i]
            nextI = intervals[i+1]

            # Now compare curr *endtime* with next starttime
            if currI.end > nextI.start:
                return False

        return True





