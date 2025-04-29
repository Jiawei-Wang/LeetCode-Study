class Solution:
    def maxDepth(self, s: str) -> int:
        best = 0
        curr = 0
        for char in s:
            if char == "(":
                curr += 1
                best = max(best, curr)
            elif char == ")":
                curr -= 1
        return best
        