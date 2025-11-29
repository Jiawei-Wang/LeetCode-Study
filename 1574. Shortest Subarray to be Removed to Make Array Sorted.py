class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # find the first peak and the last valley
        # more formally:
        # left: longest non-decreasing prefix
        # right: longest non-decreasing suffix
        n = len(arr)
        left = 0
        right = n - 1

        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # corner case: if first peak is last element, the whole array is already sorted
        if left == n - 1:
            return 0

        while right > left and arr[right - 1] <= arr[right]:
            right -= 1

        # everything between 0 to left is sorted
        # everything between right to n is sorted
        # but we don't know relationship between arr[left] and arr[right]

        # now we have the worse possible answer:
        # just keep the longest one between the two by deleting everything 
        # after first peak or deleting everything before last valley 
        ans = min(n - left - 1, right)

        # now use sliding window to get better result
        # we want to find all pairs i, j
        # i in 0 to left
        # j in right to n
        # where arr[i] <= arr[j]
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans