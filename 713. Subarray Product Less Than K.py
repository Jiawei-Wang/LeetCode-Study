class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 1 <= nums[i] <= 1000 so no product can be < 1
        if k <= 1: 
            return 0
            
        l = 0
        total = 1
        counter = 0
        
        for r in range(len(nums)):
            total *= nums[r]
            
            while total >= k:
                total //= nums[l]
                l += 1
                # if nums[r] already >= k then l will stop at r + 1
            
            counter += (r - l + 1)
            
        return counter