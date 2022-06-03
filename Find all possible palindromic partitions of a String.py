# start from every index, find every palindrome
class Solution:
    def allPalindromicPerms(self, s):
        ans = []
        
        # helper gets all palindromes starting from i and j (including j)
        def helper(i, j):
            if s[i] == s[j]:
                ans.append(s[i:j+1])
            i -= 1
            j += 1
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    ans.append(s[i:j+1])
                    i -= 1
                    j += 1
                else:
                    return
            
        for i in range(len(s)-1):
            helper(i, i)
            helper(i, i+1)
        helper(len(s)-1,len(s)-1)
        return ans


# dp
class Solution:
    def allPalindromicPerms(self, s):
        ans = [char for char in s]
        dp = [[0] * len(s) for i in range(len(s))] # dp[i][j] = 1 表示从i到j的substring（包含j）为palindrome
        for i in range(len(s)):
            dp[i][i] = 1
            
        for i in range(len(s)-1, -1, -1): # 一个非常重要的点是：这是bottom up dp，所以必须从小往大走
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        ans.append(s[i:j+1])
        return ans