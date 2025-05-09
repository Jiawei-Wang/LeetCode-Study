# sum of all possible subarrays
# n^3
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        total = 0
        for i in range(1, length+1, 2):
            for j in range(length-i+1):
                total += sum(arr[j:j+i])
        return total


# math
class Solution:
    def sumOddLengthSubarrays(self, A):
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res

    def sumOddLengthSubarrays(self, A):
        return sum(((i + 1) * (len(A) - i) + 1) // 2 * a for i, a in enumerate(A))

