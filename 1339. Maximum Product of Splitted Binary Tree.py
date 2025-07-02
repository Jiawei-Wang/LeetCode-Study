# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use a hashmap
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # key: node
        # value: [node.val, left subtree sum, right subtree sum]
        hashmap = dict() 

        def helper(node):
            if not node.left and not node.right:
                hashmap[node] = [node.val, 0, 0]
                return node.val
            
            left_sum = right_sum = 0
            if node.left:
                left_sum = helper(node.left)
            if node.right:
                right_sum = helper(node.right)
            hashmap[node] = [node.val, left_sum, right_sum]

            return left_sum + node.val + right_sum
        
        # call the helper to build the hashmap, and also get whole tree sum
        total = helper(root)

        # find the best in the hashmap
        best = 0
        for key, value in hashmap.items():
            best = max(best, (total-value[2])*value[2], (total-value[1])*value[1])
        return best % (10**9 + 7)


# two passes without hashmap
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = total = 0

        def helper(node):
            if not node: return 0
            left, right = helper(node.left), helper(node.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + node.val

        total = helper(root)
        helper(root)
        return self.res % (10**9 + 7)