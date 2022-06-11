# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input：一个root node和一个interger，找到所有从root到leaf总和为这个interger的路径，将路径上每个node的值放入答案中
"""
举例：
       1
    2     3
  4   x 3   x
目标是7
则答案应该为：[[1,2,4],[1,3,3]]

思考：因为这个tree不是有序的，任何一个node可能是任何值（可正可负），所以必须DFS完全遍历
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        # 对于一个node，我们关心它，从root到它的总和，以及此条路径
        def helper(node, cur, path):
            if not node.left and not node.right and cur+node.val == targetSum:
                ans.append(path+[node.val])
                return
            
            if node.left:
                helper(node.left, cur+node.val, path+[node.val])
            if node.right:
                helper(node.right, cur+node.val, path+[node.val])
            
        helper(root, 0, [])
        return ans