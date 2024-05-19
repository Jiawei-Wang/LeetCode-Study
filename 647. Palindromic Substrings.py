# 使用 Longest palindromic Sbustring中的两个解法：two pointer和dp

# two pointer
class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s, i, j):
            count = 0
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
                count += 1
            return count # 即使是最后一次循环，只有当s[i] == s[j]时才会+1，所以这里在返回时不需要count-1
        
        ans = 0
        for i in range(len(s)):
            ans1 = helper(s, i, i)
            ans2 = helper(s, i, i+1) 
            ans += ans1 + ans2
        return ans
        
"""
一开始写答案时使用了
for i in range(0, len(s), 2):
    ans2 = helper(s, i, i+1)
但是忘了考虑 j 永远比 i 大1
所以对于偶数substring，每次只会检查以 i 为起点的向后一格的对称轴，所以没必要步进2步
"""
        

# dp
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n): # 2d list只需要填满半边即可，因为 j 不可能小于 i，没有[j, i]这样的substring存在
                
                # 无论i和j是否相同（即它俩是否指向同一元素），它俩值必须相等，才能满足palindrome第一条件
                # 第二条件是：substring长度为1或2（这里[i, j]是两侧全包含），或者内层已经验证是palindrome
                dp[i][j] = s[i] == s[j] and ((j-i) < 2 or dp[i+1][j-1])
                
                ans += dp[i][j]
        return ans


class Solution:
    def countSubstrings(self, s: str) -> int:
            n = len(s)
            palindrome = [[0] * n for _ in range(n)] # palindrome[i][j] = True: s[i:j+1] is palindrome
            
            count = 0
            for i in range(n-1, -1, -1):
                for j in range(i, n):
                    # if string length = 1 (j==i) or = 2: palindrome[i][j] = s[i] == s[j]
                    # if string length >= 3: palindrome[i][j] = s[i] == s[j] and palindrome[i+1][j-1]
                    palindrome[i][j] = s[i] == s[j] and ((j-i+1) < 3 or palindrome[i+1][j-1])
                    count += palindrome[i][j] # 5 + True = 6

            return count