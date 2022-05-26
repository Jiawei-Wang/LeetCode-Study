# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder的第一个元素永远是root
        # inorder中在root前的元素永远是left subtree，之后的元素永远是right subtree
        # 重复此循环
        if inorder: 
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind]) 
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root