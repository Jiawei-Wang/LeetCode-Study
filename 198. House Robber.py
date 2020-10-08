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
