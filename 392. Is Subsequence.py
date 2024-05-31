class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for char in t:
            if start == len(s):
                return True
            if char == s[start]:
                start += 1

        return start == len(s)