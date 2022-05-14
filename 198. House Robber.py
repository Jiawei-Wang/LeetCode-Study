# 解法1：Recursive + memo (top-down)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 返回答案
        return self.get(nums, len(nums)-1)

    def get(self,nums,i):
        # array初始化
        memo = [-1] * (len(nums)+1)

        if i <0: return 0
        if memo[i] >= 0: return memo[i]

        result = max(self.get(nums,i-2)+nums[i], self.get(nums,i-1))
        memo[i] = result

        return result


# 解法2：Iterative + memo (bottom-up)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        memo = [0] * (len(nums)+1)
        memo[1] = nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i],memo[i-1]+val)
        return memo[len(nums)]


# 解法3：Iterative + 2 variables (bottom-up)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        neighbor = 0
        former = 0
        for i in nums:
            temp = neighbor
            neighbor = max(former+i,neighbor)
            former = temp
        return neighbor
        

# 05-14-2022
"""
# 一维dp，难点在于找到步进的逻辑
# https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
# 不需要同时考虑一个房子的前后邻居，只需要考虑之前的邻居即可：
# 如果选择nums[i]，则必须跳过nums[i-1]
# 如果不选择nums[i]，则此位置总金额和上一个位置相同
# rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
"""

# recursion
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, i):
            if i < 0: # 使用这个来规避nums[i]越界corner case
                return 0 
            return max(helper(nums, i-2)+nums[i], helper(nums,i-1))
        return helper(nums, len(nums)-1)


# recursion + memo: 和recursion相比，区别在于直接从memo中读取位置信息
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums)+1)
        
        def helper(nums, memo, i):
            if i< 0:
                return 0
            if memo[i] >= 0:
                return memo[i]
            result = max(helper(nums, memo, i-2)+nums[i], helper(nums, memo, i-1))
            memo[i] = result
            return result
        
        return helper(nums, memo, len(nums)-1)


# iteration + memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = [0, nums[0]] # 第一个元素是dummy，第二个元素对应的是nums中的第一个元素
        for i in range(2, len(nums)+1):
            memo.append(max(memo[i-1], memo[i-2]+nums[i-1])) # memo比nums在头部多一个元素，所以i的值要相对应进行调整
        return memo[-1]


# iteration with O(1) time
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        for i in nums:
            tmp = left
            left = max(right+i, left)
            right = tmp
        return left