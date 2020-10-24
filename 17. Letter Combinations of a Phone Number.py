# 解法1: backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # corner case
        if not digits:
            return []
        
        # m is the hashmap; ret is the answer list
        m = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        ret = []
        
        # path初始化为空string
        self.dfs(m, digits, "", ret)
        return ret
    
    def dfs(self, m, digits, path, ret):
        # 当digits被遍历完时, 将此时的path放入res, 返回上一层
        if not digits:
            ret.append(path)
            return 
        # 对此层的数字对应的每个字符, 依次进行recursion
        for c in m[digits[0]]:
            # 每一层移动到digits下一位, path加上当前的字符
            self.dfs(m, digits[1:], path+c, ret)