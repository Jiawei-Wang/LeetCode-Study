class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if not nums[0]:
            return 0
        else:
            cur = nums[0]//abs(nums[0])
        
        for i in nums[1:]:
            if not i:
                return 0
            else:
                cur *= (i//abs(i))
        return cur