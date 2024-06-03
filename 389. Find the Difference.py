class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = dict()
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
            counter[t[i]] = counter.get(t[i], 0) - 1
        counter[t[-1]] = counter.get(t[-1], 0) - 1
        
        return [key for key, value in counter.items() if value][0]
