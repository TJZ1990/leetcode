# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        pos = 0
        while pos < len(intervals) and newInterval.start > intervals[pos].end:
            pos += 1
            
        if pos < len(intervals):
            newInterval.start = min(newInterval.start, intervals[pos].start)
    
        while pos < len(intervals) and newInterval.end >= intervals[pos].start:
            newInterval.end = max(newInterval.end, intervals[pos].end)
            intervals.pop(pos)
        
        intervals.insert(pos, newInterval)
        
        return intervals
            
        
        
        
        
        
