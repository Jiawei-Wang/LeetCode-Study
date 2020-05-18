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
