class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = [int(x) for x in str(n)]
        return sum(n[::2]) - sum(n[1::2])