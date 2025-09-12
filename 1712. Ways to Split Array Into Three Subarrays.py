# prefix sum + binary search: nlogn
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # prefix sums
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        # iterate over left split
        ans = 0
        for i in range(n - 2):  # left must end before n-2
            left_sum = pre[i + 1]

            # let j be the end of the middle subarray
            # so the valid range for j would be
            # left <= mid: pre[i+1] <= pre[j+1] - pre[i+1]
            # aka: pre[j+1] >= 2* pre[i+1]
            # mid <= right: pre[j+1] - pre[i+1] <= pre[n] - pre[j+1]
            # aka: pre[j+1] <= (pre[n] + pre[i+1])/2

            # lower bound: first j where pre[j+1] >= 2 * left_sum
            l = bisect_left(pre, 2 * left_sum, i + 2, n)

            # upper bound: last j where pre[j+1] <= (pre[n] + left_sum) // 2
            r = bisect_right(pre, (pre[n] + left_sum) // 2, i + 2, n) - 1

            if l <= r:
                ans = (ans + (r - l + 1)) % MOD

        return ans