"""
2024:
key is to NOT miss any element
1. pick range size: all elements
2. pick stop sign: low = high, so while statement should be: low < high
3. pick mid: lower mid, so it should be < target to prevent infinite loop
4. pick new low/high: < target so low = mid + 1
5. return when loop exits: return low
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low if nums[low] == target else -1\


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low+1)//2 # if we want to use higher mid
            if nums[mid] > target: # we need to use this to prevent missing any element and getting into infinite loop
                high = mid - 1
            else:
                low = mid
        return low if nums[low] == target else -1