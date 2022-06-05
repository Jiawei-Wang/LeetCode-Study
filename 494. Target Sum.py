'''
1. repeat question
2. clarify assumption
    1）至少1个num
    2）nums均不为负
    3）+0和-0算两种（阅读第2条时突然想到然后验证得知，面试时需要和考官确认）
3. go through example
4. talk about DSA:
    1) decision tree：2^n
    2) dp: decision tree with caching: n*t, t为所有可能答案的范围（全减 ~ 全加）
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # key: (index, total), value: number of ways to get to target from index with total
        d = {}
        
        def helper(i, total):
            # base case
            if i == len(nums): # 走到头时就检查total
                return 1 if total == target else 0
            if (i, total) in d: # 如果当前位置的结果已经被计算过
                return d[(i, total)]
            
            # recursion
            d[(i, total)] = helper(i+1, total+nums[i]) + helper(i+1, total-nums[i])
        
            return d[(i, total)]
    
        return helper(0, 0)