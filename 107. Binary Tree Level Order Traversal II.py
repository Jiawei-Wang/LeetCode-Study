# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        if not root:
            return answer
        
        current_level = [root]
        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            answer.append([node.val for node in current_level])
            current_level = next_level
        
        return answer[::-1]
    