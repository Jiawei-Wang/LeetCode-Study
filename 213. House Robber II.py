class Solution:
    def rob(self, nums: List[int]) -> int:
        # 两次分别计算rob第一家和不rob第一家的结果（rob第一家 = 不rob最后一家）
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = 0
        for i in range(len(nums)-1):
            tmp = left
            left = max(right+nums[i], left)
            right = tmp
        
        left2 = 0
        right2 = 0
        for i in range(1, len(nums)):
            tmp = left2
            left2 = max(right2+nums[i], left2)
            right2 = tmp
        
        return left if left >= left2 else left2