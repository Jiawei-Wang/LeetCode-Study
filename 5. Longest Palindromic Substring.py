# check every substring: n^3

# two pointer: 遍历每个元素，找到以前为轴的最长substring
# time n^2, space 1
# 与brute force的本质区别在于减少了遍历的复杂度
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # helper从i, j出发寻找中轴对称的string
        def helper(s, i, j):
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i+1: j] # 最后不满足条件被break，但上一轮依旧会步进一步，所以这里将i，j下标所指两个元素都排除
        
        ans = ""
        for i in range(len(s)):
            s1 = helper(s, i, i)
            s2 = helper(s, i, i+1) # 考虑奇偶情况
            if len(s1) > len(ans):
                ans = s1
            if len(s2) > len(ans):
                ans = s2
        return ans


