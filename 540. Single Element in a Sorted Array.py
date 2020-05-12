class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
