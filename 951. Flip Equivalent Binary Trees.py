# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS recursion
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        # if both nodes are null: equal
        # if only one of them is null: not equal
        if not r1 or not r2: 
            return r1 == r2 == None

        # if both nodes exist:
        #   if values are the same and children are the same: equal
        #   else: not equal         
        return r1.val == r2.val and ((self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right)) or
(self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)))
    

# DFS iteration
class Solution:
    def flipEquiv(self, r1: TreeNode, r2: TreeNode) -> bool:
        stk1, stk2 = [r1], [r2]
        while stk1 and stk2:
            node1, node2 = stk1.pop(), stk2.pop()
            if node1 == node2 == None: continue 
            elif not node1 or not node2 or node1.val != node2.val: return False
            
            if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
                stk1.extend([node1.left, node1.right])
            else:
                stk1.extend([node1.right, node1.left])
            stk2.extend([node2.left, node2.right])
        return not stk1 and not stk2


# BFS
class Solution:
    def flipEquiv(self, r1: TreeNode, r2: TreeNode) -> bool:
        dq1, dq2 = map(collections.deque, ([r1], [r2]))
        while dq1 and dq2:
            node1, node2 = dq1.popleft(), dq2.popleft()
            if node1 == node2 == None: continue 
            elif not node1 or not node2 or node1.val != node2.val: return False

            if node1.left == node2.left == None or node1.left and node2.left and node1.left.val ==  node2.left.val:
                dq1.extend([node1.left, node1.right])
            else:
                dq1.extend([node1.right, node1.left])
            dq2.extend([node2.left, node2.right])
        return not dq1 and not dq2