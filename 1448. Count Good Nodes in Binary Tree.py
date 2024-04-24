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


# 2024
# dfs with no extra data structure 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        
        def dfs(node, current_max):
            nonlocal count
            if not node:
                return
            if node.val >= current_max:
                count += 1
        
            new_max = max(current_max, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        start_max = float('-inf')
        dfs(root, start_max) # start from root: empty path, no current_max value
        return count

# bfs with stack: for each node, we compare (node.val) with (current path max value), then pass updated max to child nodes
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        queue = deque([(root, float("-inf"))]) # one tuple inside a list, list is then turned into queue 
        
        while queue:
            node, current_max = queue.pop() # every element in queue is a tuple: (node, current path max value)
            if node.val >= current_max: 
                count += 1
            new_max = max(current_max, node.val) # update current path max value and give to child nodes
            
            if node.left: 
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return count