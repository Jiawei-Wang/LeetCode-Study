class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        
        # newInterval和其他元素之间可能出现的关系：
        # 1.元素头 元素尾 newInterval头 newInterval尾
        # 2.元素头 newInterval头 元素尾 newInterval尾
        # 3.元素头 newInterval头 newInterval尾 元素尾
        # 4.newInterval头 元素头 newInterval尾 元素尾
        # 5.newInterval头 newInterval尾 元素尾
        # 1和5不需要进行操作
        # 2、3、4需要将两者融合
        for i in intervals:
            if i[1] < s: # 1.
                left.append(i)
            elif i[0] > e: # 5.
                right.append(i)
            else: 
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [[s,e]] + right