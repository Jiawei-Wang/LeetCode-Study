class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs) == 1:
            return prefix
        
        for i in range(1, len(strs)):
            n = min(len(prefix), len(strs[i]))
            cur = ''
            target = strs[i]
            for j in range(n):
                if prefix[j] == target[j]:
                    cur += target[j]
                else:
                    break
            prefix = cur
            
            if i == len(strs)-1:
                return cur


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for i in range(1,len(strs)): # 即使strs长度为1也不会出现越界情况
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1] # 在当前string中调用find(prefix)，如果返回值不为0，则让prefix长度减一（从尾部开始），直到为0，此时检查prefix是否还剩元素
                if not prefix:
                    return ""
        return prefix