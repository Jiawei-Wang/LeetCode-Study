# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 和第235 Lowest Common Ancestor of a Binary Search Tree相比，没有BST结构，无法单纯使用value对比来找到位置


# 解法一：找到从root到p的路径，和root到q的路径，两个路径对比取最后一个相同的元素
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(node, path, key): 
            # node: 进入此循环时遍历到的node
            # path：上一轮循环结束时获得的path
            # value：我们要寻找的value
            if not node:
                return False
            if node == key:
                return path + [node]
            
            return findPath(node.left, path+[node], key) or findPath(node.right, path+[node], key)
        
        path_p = findPath(root, [], p)
        path_q = findPath(root, [], q)

        lp = len(path_p)
        lq = len(path_q)
        n = min(lp, lq)
        
        for i in range(n):
            if path_p[i] != path_q[i]:
                return path_p[i-1]
        
        return path_p[-1] if lp < lq else path_q[-1]