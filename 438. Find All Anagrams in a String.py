# 找到s中所有是p的anagram的substring，并返回它们的起始下标


# 遍历 + sort
# 超时
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 思路：在s中遍历所有长度等于p的substring，如果相同则加进去
        ans = []
        new = sorted(p)
        if not s or not p or len(s)<len(p):
            return ans
        for i in range(len(s)-len(p)+1):
            if sorted(s[i:len(p)+i]) == new:
                ans.append(i)
        return ans


# 遍历所有长度为p的substring（O(n))，每个和p使用counter进行对比(O(n))
# time len(s) * len(p), space len(s) * len(p) （每个substring都要使用一个counter）
# 超时
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        
        target = [0] * 26
        for c in p:
            target[ord(c)-ord('a')] += 1
        
        for i in range(len(s)-len(p)+1):
            substring = s[i: i+len(p)]
            cur = [0] * 26
            for c in substring:
                cur[ord(c)-ord('a')] += 1
            
            if cur == target:
                ans.append(i)
        
        return ans


# 优化版本，主要优化点在于：不用每次都重新检查substring，只需要对dictionary进行很小的维护即可
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res


# 2024 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        target = dict()
        for char in p:
            if char not in target:
                target[char] = 1
            else:
                target[char] += 1
        
        for i in range(len(p)):
            char = s[i]
            if char in target:
                target[char] -= 1
            else:
                target[char] = -1
        
        def empty(target):
            for key, value in target.items():
                if value:
                    return False
            return True

        answer = []
        if empty(target):
                answer.append(0)
        for i in range(len(p), len(s)):
            new = s[i]
            old = s[i-len(p)]
            if new in target:
                target[new] -= 1
            else:
                target[new] = -1
            if old in target:
                target[old] += 1
            else:
                target[old] = 1
            if empty(target):
                answer.append(i-len(p)+1)
        
        return answer
            


        