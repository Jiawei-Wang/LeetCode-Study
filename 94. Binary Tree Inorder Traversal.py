# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recurstion
class Solution:
    # inorder：左中右
    # 对于每一个node而言，返回顺序是它的左子树，自身，右子树
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self,root,ans):
        if root:
            if root.left:
                self.helper(root.left,ans)
            ans.append(root.val)
            if root.right:
                self.helper(root.right,ans)


# iteration
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


# 05-24-2022
# recursion
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, ans):
            if not node:
                return
            helper(node.left, ans)
            ans.append(node.val)
            helper(node.right, ans)
            return
        
        ans = []
        helper(root,ans)
        return ans


# 对recursion的优化
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node): # 不需要ans因为ans是全局变量
            if not node:
                return 
            helper(node.left)
            ans.append(node.val)
            helper(node.right)
            # 不需要return
        
        ans = []
        helper(root)
        return ans


# iteration
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
