# greedy: sort + keep interval that ends earlier than others
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        cnt = 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            # 每次发现一个元素与当前目标不重叠
            if s >= end: 
                end = e # 将当前目标的尾部更新为此元素尾部
            else: 
                cnt += 1 # 如果重叠则去掉
        return cnt


# greedy
# first: sort
# second: go over all elements:
# if two overlap: remove the one that ends behind
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # sort by both first element and second element
        res = 0
        prevEnd = intervals[0][1] # use first interval as starting point
        for start, end in intervals[1:]:
            if start >= prevEnd: # if no overlap
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd) # if two overlap, remove second one
        return res
