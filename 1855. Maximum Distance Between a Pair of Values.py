# binary search
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n2 = len(nums2)
        ans = 0

        for i, x in enumerate(nums1):
            low, high = i, n2 - 1   # j must be ≥ i

            # find the largest j with nums2[j] >= x
            best = -1
            while low <= high:
                mid = (low + high) // 2
                if nums2[mid] >= x:
                    best = mid
                    low = mid + 1  # try to go farther right
                else:
                    high = mid - 1

            if best != -1:
                ans = max(ans, best - i)

        return ans
