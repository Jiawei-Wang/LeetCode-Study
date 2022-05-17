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


"""
dp: time n^2 space n^2 
基本逻辑：和brute force相比，遍历时间不变，将之前计算过的值保存下来在下次遍历时省去计算时间

# https://www.youtube.com/watch?v=TLaGwTnd3HY&ab_channel=GeeksforGeeks
用L(0, 6)指代从0到6这个substring中最长的palindrome
则L(0,6)=L(0,5)+2 if s[0]==s[6] else L(0,6)=max(L(0,5),L(1,6) 
两个指针i, j各需要一维list，所以使用一个2d list
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]

        #filling out the diagonal by True
        for i in range(len(s)):
            dp[i][i] = True # 字符本身是一个长度为1的palindrome
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)): # j starts from the i location : to only work on the upper side of the diagonal   
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    # if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom


