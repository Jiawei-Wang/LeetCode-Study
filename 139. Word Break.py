# 如果能找到一种分割s的方法，使得所有substring都是wordDict中的元素，返回True，否则False
# 逻辑：类似于爬梯子/硬币组合，我们想找出一个可能的组合
# s = "leetcode"
# words = ["leet", "code"]
# d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
# d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                # 如果当前 d 的subarray：1.的substring能在wordDict中找到，2.且前面部分已经被证明True或者前面是整个array的头
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]