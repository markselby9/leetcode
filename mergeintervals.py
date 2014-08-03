__author__ = 'fengchaoyi'
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals == []: return []
        if len(intervals) == 1: return intervals
        intervals.sort(key=lambda segment:segment.start)
        i=0
        while i < len(intervals):
            if i == len(intervals)-1:
                break;
            elif intervals[i].end >= intervals[i+1].start:
                if intervals[i+1].end < intervals[i].end:
                    intervals.remove(intervals[i+1])
                else:
                    intervals[i].end = intervals[i+1].end
                    intervals.remove(intervals[i+1])
            else:
                i+=1
        return intervals

sol = Solution()
list = [Interval(1,5), Interval(1,2), Interval(2,4)]
for seg in sol.merge(list):
    print seg.start, " ", seg.end, ";"
