"""
Description
Given an array of meeting time intervals consisting of 
start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

Corner case: (0,8),(8,10) is not conflict at 8

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
"""


class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            first = intervals[i-1]
            second = intervals[i]
            if first.end > second.start:
                return False
        
        return True


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals):
            return True

        intervals.sort(key = lambda x: x.start)
        current = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < current:
                return False
            current = intervals[i].end
        return True
