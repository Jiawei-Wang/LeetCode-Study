class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = len(nums)
        for loops in range(length-1):
            for i in range(length-1, loops, -1):
                nums[i] = (nums[i-1]+nums[i]) % 10
        return nums[-1]


# math
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        C = 1  # C(n-1, 0)

        for i in range(n):
            ans = (ans + C * nums[i]) % 10

            # compute next binomial coefficient:
            # C(n-1, i+1) = C(n-1, i) * (n-1-i) / (i+1)
            if i < n-1:
                C = C * (n-1-i) // (i+1)

        return ans
