"""
below solution is incorrect, it will fail on this: 
                      5
                4          6
                         3   7
and return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: # if node has no child
            return True
        elif root.left and root.right: # if node has both children
            if not (root.left.val < root.val < root.right.val):
                return False
            else:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
        elif root.left and not root.right: # if node has left child
            if not root.left.val < root.val:
                return False
            else:
                return self.isValidBST(root.left)
        else: # if node has right child
            if not root.right.val > root.val:
                return False
            else:
                return self.isValidBST(root.right)
"""


"""
correct solution: find the available value range for all nodes
for example: 
                      5
                4          6
                         3   7
for root: -inf < 5 < inf
for 4: -inf < 4 < 5
for 6: 5 < 6 < inf
for 7: 6 < 7 < inf
for 3: 5 < 3 < 6: return False
"""
class Solution:
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf")) 

    def check_bst(self, node, left, right): 
        if not node:
            return True

        if not left < node.val < right:
            return False

        # if node exists and node.val is within range
        return (self.check_bst(node.left, left, node.val)  
                and self.check_bst(node.right, node.val, right))
    
    '''
    left and right are NOT child node values, they are available value range
    初始时left = -inf，right = inf (root doesn't have value range)
    每次进入下一层时，根据左右subtree，将当前node的值更新为新的限制条件
    比如root的左子node的限制为：-inf < value < root.val
    假设root = 10, 此node = 5，则它的右子node的限制为 5 < value < 10
    '''


# 2025
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, left, right):
            if not node:
                return True
            
            if left < node.val < right:
                return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
            else:
                return False
            
        return isValid(root, -float("inf"), float("inf"))
        