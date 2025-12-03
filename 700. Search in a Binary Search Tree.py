# direct recursion in the main function
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# recursion via a separate helper function
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self._helper(root, val)
        
    def _helper(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node:
            return None
        
        if node.val == val:
            return node
        elif node.val > val:
            return self._helper(node.left, val)
        else:
            return self._helper(node.right, val)


# recursion via a nested helper function
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not node:
                return None
            
            if node.val == val:
                return node
            elif node.val > val:
                return helper(node.left, val)
            else:
                return helper(node.right, val)
        return helper(root, val)
        
    
