class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == "0" else 0
        right = s[1:].count("1")
        score = left + right
        best = score
        for i in range(1, len(s)-1):
            char = s[i]
            if char == "0":
                score += 1
                best = max(best, score)
            else:
                score -= 1
                best = max(best, score)
        return best


        