# given an itnervalsk, determine if a person could attend all meetings
# sort by the end time 
# start from the beginning, if next start time is < curr end time return false
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)==1: 
            return True
        intervals.sort(key=lambda x:x[1]) # sort by end time
        for i in range(1, len(intervals)): 
            if intervals[i][0]<intervals[i-1][1]: 
                return False
        return True
