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


"""
2026
find a subset of non-overlapping jobs that maximizes the profit
this is a weighted interval scheduling problem variation

brute force: take or leave decision tree
1. sort jobs by start time
2. for each job: 
        leave it and move to the next job
        take it and find the next available job using binary search
"""
from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # 1. Combine and sort jobs by their start time
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        
        # Extract sorted start times so we can binary search on them later
        sorted_start_times = [j[0] for j in jobs]
        
        def find_max_profit(i):
            # Base Case: No more jobs left to consider
            if i >= n:
                return 0
            
            # Choice 1: Leave the current job
            # We just move to the next index (i + 1)
            leave_profit = find_max_profit(i + 1)
            
            # Choice 2: Take the current job
            current_start, current_end, current_profit = jobs[i]
            
            # Find the next job that starts >= current_end using binary search
            next_job_index = bisect_left(sorted_start_times, current_end)
            
            take_profit = current_profit + find_max_profit(next_job_index)
            
            # Return the best decision
            return max(leave_profit, take_profit)
            
        return find_max_profit(0)


from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
            
        # 1. Zip, sort by start time, and unpack
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        
        # We need a separate list of start times to use binary search (bisect_left)
        sorted_start_times = [j[0] for j in jobs]
        
        # 2. Initialize the DP table
        # dp[i] represents the max profit possible from job i to the end
        # Size is n + 1 so that dp[n] acts as our base case (0 profit)
        dp = [0] * (n + 1)
        
        # 3. Fill the table backward
        for i in range(n - 1, -1, -1):
            # Choice 1: Leave the current job
            leave_profit = dp[i + 1]
            
            # Choice 2: Take the current job
            current_profit = jobs[i][2]
            current_end = jobs[i][1]
            
            # Binary search manually for the next job that starts >= current_end
            next_job_index = bisect_left(sorted_start_times, current_end)
            
            take_profit = current_profit + dp[next_job_index]
            
            # Store the optimal decision for state i
            dp[i] = max(leave_profit, take_profit)
            
        # dp[0] holds the max profit looking at all jobs from index 0 onward
        return dp[0]