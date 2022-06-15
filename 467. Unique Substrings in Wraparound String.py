# 其实这道题等同于问：给一个string p，其中有多少个substring是按字母顺序依次排列的
# 符合条件的substring：a, b, ab, xy, za （单个字母，连续的字母，尾部接续头部的字母）
# 不符合条件的substring：ac, ba （中间有缺漏，顺序错误）

# 暴力检查每个substring
# 同时要使用set来防止重复
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if len(p) == 1:
            return 1
        
        def valid(s): # 不需要检查单个char，所以这里的s一定都至少长度为2
            for i in range(0, len(s)-1):
                if ord(s[i]) != ord(s[i+1]) - 1 and ord(s[i]) != ord(s[i+1]) + 25:
                    return False
            return True
        
        visited = set(char for char in p)
        
        for i in range(len(p)-1):
            for j in range(i+2, len(p)+1):
                cur = p[i:j]
                if valid(cur):
                    visited.add(cur)
        return len(visited)


# 暴力解 + cache：
# 存储已计算部分然后下次长度+1时直接调用
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        
        if n == 1:
            return 1
        
        ans = set(char for char in p)
        
        def valid(s): # 不需要检查单个char，所以这里的s一定都至少长度为2
            if s[0:len(s)-1] in ans and (ord(s[-2]) == ord(s[-1]) - 1 or ord(s[-2]) == ord(s[-1]) + 25):
                ans.add(s)
                return True
                
            for i in range(0, len(s)-1):
                if ord(s[i]) != ord(s[i+1]) - 1 and ord(s[i]) != ord(s[i+1]) + 25:
                    return False
                
            return True
        
        # 最短2，最长len(p)
        for length in range(2, n+1):
            for i in range(0, n-length+1):
                cur = p[i:i+length]
                if valid(cur):
                    ans.add(cur)
        return len(ans)


"""
DP：
1. 如果我们想找到所有substring，我们可以去找（所有以某个字母为末尾的substring），然后将此方法重复在26个字母上即可
2. 所有以字母X为结尾的substring，已经全部被包含在最长的substring中（举例：bcdecde，bcde中已经包含所有以e结尾的substring，后面的cde没有必要再去查看）
注：所有substring指的都是符合条件的substring
"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        count = [0] * 26 # 记录以每个字母结尾的符合条件的substring总数
        
        maxLenCur = 0 # 最长substring
        
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == -25):
                maxLenCur += 1
            else:
                maxLenCur = 1
            
            index = ord(p[i]) - ord('a')
            count[index] = max(count[index], maxLenCur)
            
        return sum(count)