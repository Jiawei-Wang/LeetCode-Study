# TLE
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = len(s)
        answer = set()
        for x in range(0, l-2):
            for y in range(x+1, l-1):
                for z in range(y+1, l):
                    if s[x] == s[z]:
                        answer.add(s[x]+s[y]+s[z])
        return len(answer)


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashmap = dict()
        for char in s:
            for key, value in hashmap.items():
                value.append(char)
            if char not in hashmap:
                hashmap[char] = []
            
        count = 0
        for key, value in hashmap.items():
            for i in range(len(value)-1, -1, -1):
                if key == value[i]:
                    count += len(set(value[:i]))
                    break
        return count
        

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [-1] * 26
        res = 0

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        for i in range(26):
            if first[i] < last[i]:
                distinct_chars = set(s[first[i]+1:last[i]])
                res += len(distinct_chars)

        return res