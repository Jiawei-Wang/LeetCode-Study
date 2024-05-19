# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# we know: for a tree: 
# preorder的第一个元素是root
# inorder中在root前的元素是left subtree，之后的元素是right subtree
# so we can:
# 1. get the root
# 2. remove root from both lists
# 3, recursively build left subtree and right subtree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder: 
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind]) 
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root