class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                ans += len(set(nums[i:j]))**2
        return ans