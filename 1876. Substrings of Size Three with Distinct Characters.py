class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(2, len(s)):
            count += 1 if len(set(s[i-2:i+1])) == 3 else 0
        return count