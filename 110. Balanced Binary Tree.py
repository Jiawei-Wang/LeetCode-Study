# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right))+1
        
        left = depth(root.left)
        right = depth(root.right)
        return abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


# 优化
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            
            # 如果当前node的左右子树不平衡，则flag
            if left == -1 or right == -1 or abs(left-right)>1:
                return -1
            
            return max(left,right)+1
        
        return helper(root) != -1
    
    """
    对于答案的思考：
    首先是caching减少时间复杂度
    对于helper里面的内容：
        一开始走到最底下，if statement为False，所以底层node高为1
        从倒数第二层开始，此时left，right都有值了，就进入if statement判断，如果任何一个子树不平衡，自身也会被标为不平衡
        然后逐层往上，只要是子树被标记的，自身也会被标记
        所以最后如果root ！= -1，那么它的两个子树必然不是 -1
    """