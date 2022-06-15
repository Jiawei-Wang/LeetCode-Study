# nums中每个元素均不同，找到组成target的所有组合
# 1. 一个元素可以被多次使用
# 2. 使用顺序不同被视为不同组合，举例 [1,3] 和 [3,1] 被视为两种组成4的方法

# recursion：任何一个值都可以被除去然后再次使用更新的target去重新遍历list
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 题目限定nums最小长度为1，每个元素都为正整数，且target也为正整数，所以target==0时必然不存在res=0
        if target == 0:
            return 1
        
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.combinationSum4(nums, target -nums[i])
        
        return res


# top down dp
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1) # -1表示无法到达，0表示没有组合
        dp[0] = 1
        
        def helper(nums, target):
            if dp[target] != -1:
                return dp[target]
            res = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    res += helper(nums, target - nums[i])
            
            dp[target] = res
            return res
        
        
        return helper(nums, target)


# bottom up dp
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb = [0] * (target + 1)
        comb[0] = 1
        for i in range(1, len(comb)):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    comb[i] += comb[i - nums[j]]
        
        return comb[target]