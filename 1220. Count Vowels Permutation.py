"""
https://www.youtube.com/watch?v=VUVpTZVa7Ls&ab_channel=NeetCode

逻辑：
1. 使用decision tree，当层数少时，可以穷举
2. 穷举时发现当前层选定一个字母后，下一层可以选的字母总数受规则限制
3. 此时可以建立每一层间的关系：此层可选字母受限于上一层，并对下一层产生影响
4. 将此拓展为一个2d list

     1    2    
a    1    3
e    1    以此类推
i    1
o    1
u    1

解释：
第一层可以选择任何字母，所以此层数量均为1
第二层以a为例，若想用a填充第二层，那么第一层必须是e，i，u其中一者，所以
dp[2][a] = dp[1][e] + dp[1][i] + dp[1][u]
其他4个字母也遵循其对应规则

time: O(n)
space：O(n)
解释：每层进行5次计算，共n层
还可以通过只保留2层计算结果的方式来进一步压缩space complexity
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[],[1,1,1,1,1]]
        a,e,i,o,u = 0,1,2,3,4
        mod = 10**9 + 7
        
        for j in range(2,n+1):
            dp.append([0,0,0,0,0])
            dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) % mod
            dp[j][e] = (dp[j-1][a] + dp[j-1][i]) % mod
            dp[j][i] = (dp[j-1][e] + dp[j-1][o]) % mod
            dp[j][o] = dp[j-1][i]
            dp[j][u] = dp[j-1][i] + dp[j-1][o]
  
        return sum(dp[n]) % mod
        
        
        
        
        
        
        
        