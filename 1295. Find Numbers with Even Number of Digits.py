class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            j = str(i)
            if len(j) % 2 == 0:
                ans += 1
        return ans
