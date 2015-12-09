#First sort the intervals by its start.
#If two intervals overlap, join them.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        intervals.sort(key = lambda x : x.start)
        result = [intervals[0]]
        for i in intervals[1:]:
            if i.start > result[-1].end:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)
    
        return result
