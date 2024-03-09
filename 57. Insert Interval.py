# 找到第一个interval，融合，然后将后面interval全部融合，如果没找到interval则找到插入位置并插入
# 写这个答案的过程中出现了非常多的corner case报错，针对每个corner case去修改代码才通过
class Solution:
    def insert(self, l: List[List[int]], n: List[int]) -> List[List[int]]:
        if not l: # corner case：注意空list直接加入
            return [n]
        length = len(l)
        target = -1
        for i in range(length):
            # 两个元素重叠的判断：目标的头部或尾部在当前元素的范围内
            if l[i][0] <= n[0] <= l[i][1] or l[i][0] <= n[1] <= l[i][1] or \
            (l[i][0] <= n[0] and l[i][1] >= n[1]) or (l[i][0] >= n[0] and l[i][1] <= n[1]): # corner case: 注意还有一种重叠是一方被另一方全部包含
                target = i
                l[i][0] = min(l[i][0], n[0])
                l[i][1] = max(l[i][1], n[1])
                # 找到尾部最长延申位置
                j = i + 1
                while j < len(l) and l[i][1] >= l[j][0]: # corner case: 注意j越界
                    l[i][1] = max(l[i][1], l[j][1])
                    del l[j] # 因为该元素被删除，后面元素被往前挪，所以没必要 j+=1
                break
        # corner case: 注意如果遍历完都没发现interval，那么要找到在l中n应该插入的位置
        if target == -1:
            for i in range(length):
                if l[i][0] > n[0]:
                    l.insert(i, n)
                    return l
            l.append(n)
        return l


# 优化: 依旧是遍历，但是使用两个list，分别保存前面和后面不和newInterval相交的元素
# 聪明之处：判断是否相交非常繁琐，所以干脆只判断是否不相交，其余的都进行融合
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        
        # newInterval和其他元素之间可能出现的关系：
        # 1.元素头 元素尾 newInterval头 newInterval尾
        # 2.元素头 newInterval头 元素尾 newInterval尾
        # 3.元素头 newInterval头 newInterval尾 元素尾
        # 4.newInterval头 元素头 元素尾 newInterval尾
        # 5.newInterval头 元素头 newInterval尾 元素尾
        # 6.newInterval头 newInterval尾 元素头 元素尾
        # 1和6不需要进行操作
        # 2、3、4、5需要将两者融合
        
        for i in intervals:
            if i[1] < s: # 1.
                left.append(i)
            elif i[0] > e: # 6.
                right.append(i) # 第一解中漏掉的细节：因为intervals中的元素本身不相交，所以newInterval的尾部覆盖的元素，在更新后不会和下一个元素相交
            else: # 其他的不用再进行判断，肯定相交
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [[s,e]] + right


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        answer = []
        head = newInterval[0]
        tail = newInterval[1]

        for index in range(len(intervals)):
            current = intervals[index]
            # case 1: newInterval is inside an existing interval
            if current[0] <= head and current[1] >= tail: 
                return intervals
            # case 2: newInterval doesn't interact with current interval
            elif current[1] < head: # newInterval is behind current interval
                answer.append(current)
                if index == len(intervals)-1: # if current interval is the last in the list
                    answer.append(newInterval)
            elif current[0] > tail: # newInterval is in front of current interval
                answer.append([head, tail]) 
                for remain in intervals[index:]:
                    answer.append(remain)
                return answer
            # case 3: newInterval interact with current interval 
            else: 
                head = min(current[0], head)
                tail = max(current[1], tail) # we merge current interval into newInterval
                if index == len(intervals)-1: # if current interval is the last in the list
                    answer.append([head, tail]) 
            
        return answer

        