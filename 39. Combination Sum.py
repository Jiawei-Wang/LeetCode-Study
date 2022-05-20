"""
解题逻辑：decision tree
解决duplicate的方法：保证每次选择路径有两个方向：选择元素A作为此轮目标，此轮选择其他元素并保证后续轮次的选择也不会再选元素A
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, cur, total):
            """
            i: index of current element
            cur: list of selected elements
            total: sum of selected elements
            """
            if total == target: # 如果找到可能解
                res.append(cur.copy()) # copy()的原因是修改list中的元素，其他引用此list的变量的值也会发生更改
                return
            
            if i >= len(candidates) or total > target: # 如果当前cur绝对不是可能解
                return
            
            # 如果还未找到解，那么进入decision tree
            cur.append(candidates[i]) 
            dfs(i, cur, total + candidates[i]) # 重复使用当前元素
            cur.pop()
            dfs(i + 1, cur, total) # 绝不再使用当前元素
        
        res = []
        dfs(0, [], 0)
        return res