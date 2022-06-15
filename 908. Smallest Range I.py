# 给一个list，其中每个元素都可以在[-k, k]的范围内修改最多一次，找到list中（最大值和最小值的差值）的最小值
# 举例：nums = [0, 10]，k = 2，那么最小值为6，即(10-2)-(0+2)
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        Max = max(nums)
        Min = min(nums)
        return Max - Min - 2*k if Max - Min > 2*k else 0