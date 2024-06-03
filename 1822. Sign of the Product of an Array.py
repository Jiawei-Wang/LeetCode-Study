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


# 2024
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if not num:
                return 0
            if num < 0:
                count += 1 
        return -1 if count % 2 else 1
        