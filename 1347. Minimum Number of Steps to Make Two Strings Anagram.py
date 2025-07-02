class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        for index in range(len(s)):
            count[ord(s[index])-ord('a')] += 1
            count[ord(t[index])-ord('a')] -= 1
        
        total = 0
        for c in count:
            if c > 0:
                total += c
        return total