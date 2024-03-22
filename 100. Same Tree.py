# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        
        # one of p and q is None
        if not q or not p:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
    
"""
理解：recursion，每一层就三种情况：
1. 两者均不存在
2. 其中一方不存在
3. 两者均存在且值相同: 唯一一个需要进入下一层的情况
4. 两者均存在且值不同
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        
