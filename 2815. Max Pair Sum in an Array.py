class Solution:
    def maxSum(self, nums: List[int]) -> int:

        def max_digit(x):
            return max(int(d) for d in str(x))

        groups = defaultdict(list)

        for n in nums:
            d = max_digit(n)
            groups[d].append(n)

        ans = -1
        for arr in groups.values():
            if len(arr) >= 2:
                arr.sort(reverse=True)
                ans = max(ans, arr[0] + arr[1])

        return ans
