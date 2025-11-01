class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = 0
        bigger = 0
        for num in nums:
            if num < target:
                smaller += 1
            if num > target:
                bigger += 1
        return [x for x in range(smaller, len(nums)-bigger)]
        