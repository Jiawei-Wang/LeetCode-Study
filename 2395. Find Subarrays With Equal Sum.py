class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)-1):
            pair = nums[i] + nums[i+1]
            if pair in seen:
                return True
            seen.add(pair)
        return False