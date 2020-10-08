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
