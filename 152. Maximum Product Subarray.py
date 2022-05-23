class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 因为不确定后面的元素是负数还是正数，所以保留当前最大和最小值
        res = max(nums)
        curMin, curMax = 1, 1 
        
        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) # 举例：[0, -1, 2]，到2前，最小值subarray为-1，最大值subarray为0，到2时最小-2，最大2
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res