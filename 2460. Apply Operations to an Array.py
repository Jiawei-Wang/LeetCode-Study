class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        print(nums)

        pos = 0 
        for x in nums:
            if x != 0:
                nums[pos] = x
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
        
        return nums