class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_valid(index):
            for i in range(index + 1, index + k):
                if nums[i] <= nums[i-1]:
                    return False
            return True
        
        
        for i in range(0, len(nums)-2*k+1):
            if is_valid(i) and is_valid(i+k):
                return True
        return False

