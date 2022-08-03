# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 读题想法：dfs，将当前路径上所有点保存下来，如果新的node>=路径上其他所有点，则将此node输出，转换路径时将node删除
# 优化：因为题目要求的是node的总数而非node的list，所以没必要去记录path的信息，而且这样也可以加快对比的速度（不需要将node和path中每个node挨个对比）
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            # 如果已经走到头
            if not node:
                return 0 
            
            # res是此node所代表的subtree的答案
            res = 1 if node.val >= maxVal else 0 # 1.检查此subtree的root是否符合条件
            maxVal = max(maxVal, node.val) # 2.更新最大值
            res += dfs(node.left, maxVal) # 3.进入左右subtree的recursion
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)