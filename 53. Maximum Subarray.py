class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


"""
理解：
我们需要返回subarray的值，所以不需要保留index的信息，记录值并找到max值即可
所以只要计算以每个element作为结尾的max subarray

对于以 i 结尾的subarray，情况如下：
其前面所有element之和为正，或者为负
如果为负，丢弃不用即可
"""


# 05-09-2022
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=5WZl3MMT0Eg&ab_channel=NeetCode
        # 逻辑：
        # 对于每个元素，计算从第一个元素到它为止的sum，最后取sum中最大值
        # 如果prefix的sum是负数，就丢弃
        # time n
        maxSubarray = nums[0] # 第一个元素的sum即为自身
        curSum = 0 # 第一个元素没有current sum
        
        for i in nums:
            if curSum < 0: # 如果这个元素前面所有元素的总和为负数，那么就丢弃
                curSum = 0
            curSum += i 
            maxSubarray = max(maxSubarray, curSum)
        return maxSubarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp
        dp = [] # dp[i] means the maximum subarray ending with nums[i]
        dp.append(nums[0])
        maxSub = dp[0]
        for i in range(1, len(nums)):
            dp.append(nums[i] + (dp[i-1] if dp[i-1]>0 else 0))
            maxSub = max(maxSub, dp[i])
        return maxSub
        # 原先的答案是：
        # dp = [] 
        # dp[0] = nums[0]
        # 出现index越界错误，原因是初始化时没有给元素，解决办法就是使用append

       