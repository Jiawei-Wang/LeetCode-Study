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


# 优化版本，主要优化点在于：不用每次都重新sort一个substring，只需要对dictionary进行很小的维护即可
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
