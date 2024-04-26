# dp: 因为不确定后面的元素是负数还是正数，所以保留当前最大和最小值
class Solution:
    def maxProduct(self, nums: List[int]) -> int:  
        res = nums[0]
        curMin, curMax = 1, 1 
        
        """
        for each element, we have 2 options:
            1. include it in current subarray
            2. don't include it (start new subarray)
        start of the subarray doesn't matter, since we only keep the min and max
        """
        for num in nums:
            tmp = curMax
            curMax = max(curMax * num, curMin * num, num) 
            curMin = min(tmp * num, curMin * num, num)
            res = max(res, curMax) 
        return res
        """
        for example: 
        [2, 3, -2, 4]
            1. for 2: max = 2, min = 2 
            2. for 3: max = 6 (extend current subarray), min = 3 (start new subarray)
            3. for -2: max = -2 (start new subarray), min = -12 (extend current subarray)
            4. for 4: max = 4 (start new subarray), min = -48 (extend current subarray)

        [0, -1, 2]
            1. for 0: max = 0, min = 0
            2. for -1: max = 0 (extend), min = -1 (start new)
            3. for 2: max = 2 (start new), min = -2 (extend)
        """
        