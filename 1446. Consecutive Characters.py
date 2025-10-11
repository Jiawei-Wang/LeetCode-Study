class Solution:
    def maxPower(self, s: str) -> int:
        anchor = 0

        answer = 0
        for i in range(len(s)):
            current = s[i]
            if current == s[anchor]:
                answer = max(answer, i-anchor+1)
            else:
                anchor = i
        return answer
        