# dp + binary search
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1]) # 元素为一个tuple (startTime, endTime, profit)，以endTime排序
        
        dp = [[0, 0]] # 结束时间为0时profit = 0
        
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1 # 找到此job startTime的前一个job
            if dp[i][1] + p > dp[-1][1]: # 如果做此job的获利比不做大，则做
                dp.append([e, dp[i][1] + p])  # 更新当前endTime
        return dp[-1][1]