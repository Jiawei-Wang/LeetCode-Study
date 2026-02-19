# brute force: check eery subarray n^3


# better: expand from each peak n^2
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:  # peak
                l = i - 1
                r = i + 1

                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1

                ans = max(ans, r - l + 1)

        return ans


# dp: n
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        up = [0] * n
        down = [0] * n
        # up[i]: length of increasing sequence ending at i
        # down[i]: length of decreasing sequence starting at i

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1

        ans = 0
        for i in range(n):
            if up[i] > 0 and down[i] > 0:
                ans = max(ans, up[i] + down[i] + 1)

        return ans
        