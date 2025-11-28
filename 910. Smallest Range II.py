class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        # res doesn't change if we let every num in nums -= k
        # so the question becomes: we can either += 0 or += 2k to every num in nums
        # do both to every element and see if we can smaller res
        for i in range(len(nums) - 1):
            big = max(nums[-1], nums[i] + 2 * k)
            small = min(nums[i + 1], nums[0] + 2 * k)
            res = min(res, big - small)
        return res