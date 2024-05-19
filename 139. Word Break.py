# 如果能找到一种分割s的方法，使得所有substring都是wordDict中的元素，返回True，否则False
# 逻辑：类似于爬梯子/硬币组合，我们想找出一个可能的组合
# s = "leetcode"
# words = ["leet", "code"]
# d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
# d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (dp[i-len(w)] or i-len(w) == -1):
                    dp[i] = True
        return dp[-1]