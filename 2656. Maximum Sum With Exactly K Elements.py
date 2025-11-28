class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        target = max(nums)
        return (target + target + k - 1) * k // 2