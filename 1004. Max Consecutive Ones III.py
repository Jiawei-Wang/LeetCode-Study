class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        res = 0
        start = 0

        for end, num in enumerate(nums):
            if num == 0:
                zeroes += 1
            while zeroes > k:
                if nums[start] == 0:
                    zeroes -= 1
                start += 1
            res = max(res, end-start+1)
        return res