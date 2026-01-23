class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a, b = min(a, b), max(a, b)
        count = 0
        for i in range(1, a+1):
            if not a % i and not b % i:
                count += 1
        return count