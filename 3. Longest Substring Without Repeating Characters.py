class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力解：穷举所有substring，然后检查是否符合要求，O(n^3)
        
        # 优化解：遍历每个item，找出以它为起始端的符合要求的最长substring，O(n^2)
        # if not s:
        #     return 0
        # result = 1
        # for i in range(len(s)):
        #     curr = 1
        #     dic = set(s[i])
        #     j = i
        #     while j + 1 < len(s) and s[j+1] not in dic:
        #         curr += 1
        #         dic.add(s[j+1])
        #         j += 1
        #     result = max(result, curr)
        # return result
        
        # 最优解：two pointers: O(n), space: O(n)
        # 两个指针的移动逻辑如下：
        # 1. 左指针不动，右指针一直走到出现重复元素为止
        # 2. 此时移动左指针直到重复元素被排除为止
        # 3. 重复第1步
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
