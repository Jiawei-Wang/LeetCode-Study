# 读题想法:
# 1. 找出每个重复元素的substring
# 2. 将cost最高的那个保留,删除其他的
# Time: n
# Space: 1

'''
自己的解法: 通过了三个testcase,但是在提交时面对:"abaac" [1,2,3,4,5],出现错误,回头debug
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        head = 0
        tail = 0
        for index in range(len(s)):
            # 获得当前的char,以及该char的substring的首尾下标
            curr = s[index]
            head = index
            while index < len(s) and s[index] == curr:
                tail = index
                index += 1
            if tail > head:
                # 将substring的总cost,以及单个char最高cost记录下来
                total = 0
                highest = 0
                for i in range(head, tail+1):
                    total += cost[i]
                    highest = max(highest, cost[i])
                # 开销是total - highest
                ans += total -highest
            # 从tail后一个char开始继续遍历
            index = tail + 1
        return ans
'''


# 解法2
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        max_cost = 0
        sum_cost = 0

        # 遍历每个元素
        for i in range(len(s)):
            # 如果当前元素和前一个不同,将前面的cost记录下来,抹去变量的值
            if i > 0 and s[i] != s[i-1]:
                res += sum_cost - max_cost
                sum_cost = 0
                max_cost = 0

            # 不需要使用else,因为如果符合上面的if statement的条件的话,变量都是0,不发生改变
            sum_cost += cost[i]
            max_cost = max(max_cost, cost[i])

        # 将最后一个substring的cost记录下来
        res += sum_cost - max_cost

        return res


# 解法3:对解法2的代码进行简化
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res 
