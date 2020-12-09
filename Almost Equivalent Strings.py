"""
https://leetcode.com/discuss/interview-question/840988/Akuna-Quant-Researcher-OA
"""
from collections import Counter

class Solution:
    def answer(self, s, t):
        def compare(first, second):
            dic1 = dict(Counter(first))
            dic2 = dict(Counter(second))
            for e in dic1:
                if e not in dic2:
                    dic2[e] = 0
                if abs(dic1[e] - dic2[e]) > 3:
                    return False
            for e in dic2:
                if e not in dic1:
                    dic1[e] = 0
                if abs(dic1[e] - dic2[e]) > 3:
                    return False
            return True
             
        ans = []
        for i in range(len(s)):
            first = s[i]
            second = t[i]
            if compare(first, second):
                ans.append("YES")
            else:
                ans.append("NO")
        return ans

if __name__ == "__main__":
    # Should return ["YES", "NO"]
    s = ["aabaab", "aaaaabb"]
    t = ["bbabbc", "abb"]
    case1 = Solution()
    print(case1.answer(s, t))

