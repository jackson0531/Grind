# given intervals, return min intervals needed to be removed for non-overlapping purpose
# 1,10 2,3 4,5 6,7
# sort based the ending time
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        result = 0
        if len(intervals)==1: 
            return 0
        current = 1
        prev = 0
        while current < len(intervals):
            if intervals[current][0]<intervals[prev][1]: 
                result+=1
                current+=1
                # intervals.pop(current)
            else: 
                prev = current
                current+=1
        return result
