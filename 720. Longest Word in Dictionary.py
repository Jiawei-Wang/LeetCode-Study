# 题目并不是我读题后想的那样：我最初想的是，从每个string中取一个char，来组成答案
# 但是给例子：["a","ba", "bca"]，我想象的答案是'bca'，但系统给的答案是'a'
# 所以这题是挨个往后加char
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 先将list sort，短的string靠前，同长度string按字母顺序排列
        words.sort()
        
        built = set()
        ans = ''
        for w in words:
            if len(w) == 1 or w[0:len(w)-1] in built:
                ans = w if len(w) > len(ans) else ans
                built.add(w)
        
        return ans