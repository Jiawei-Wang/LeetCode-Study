# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# a path: one leaf -> node A -> another leaf
# path through root is not always the longest 
# so we need to find all paths and return the longest one
# which means we need to find longest path for every node
# for node A: the longest path is the longest left leg + node A + longest right leg
# and for parent node B: longest path = return value of A + node B + return value of child node C
# so we need to return the longest leg, which is the bigger one between two legs
# for leaf node: both legs are 0
# for other nodes: longest leg = node + max(left leg, right leg)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf") 
        
        def path(node):
            nonlocal max_path # This tells that max_path is not a local variable
            
            if node is None:
                return 0
            
            left  = max(path(node.left), 0) 
            right = max(path(node.right), 0)  
 
            max_path = max(max_path, node.val + left + right) 

            return node.val + max(left, right) 
		
        path(root) 
        return max_path	


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = -float('inf')

        def dfs(node):
            nonlocal answer
            if not node:
                return 0
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            # for the path, I have three options:
            # 1. having both legs
            # 2. having either leg
            # 3. having no leg
            answer = max(answer, max(0, left) + max(0, right) + node.val)
            # but for return value, I must pick one leg and one leg only
            return node.val + max(0, left, right)
        
        dfs(root)
        return answer