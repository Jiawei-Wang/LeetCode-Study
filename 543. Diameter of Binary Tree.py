# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
1. we want to get the length of the longest path
2. a path = longest leg of left subtree + longest leg of right subtree
3. the path across root node is not always the longest
4. so we need to get path for every node
5. there is no relation between path length for current node, and path length for node.left and node.right
6. there IS relation between longest two legs of current node, and longest two legs of node.left and node.right:
    1) longest left leg of node = 1+ max(longest left leg of node.left, longest right leg of node.left)
    2) so is right leg with node.right
7. so at each node:
    1) we calculate path length and update global longest path length
        1- only one global variable is needed (path and path don't have relation)
    2) path length is calculated based on two legs
        1- leg itself is calculated based on one subtree leg from each subtree
        2- so we only need to keep track of the longest one leg, the other one doesn't matter
"""


# revisit the problem in 2025 since I still have trouble understanding recursion well
# issue: logic is clear on paper but coding is unclear, espicially the recursion body
# whether variable is needed, what if-statement to use, how to recurse, what to return, etc
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # first: understand the question:
        # longest path doesn't need to pass root, so we need to calculate every path
        # since we only need to return one longest path, we don't need to store every path but rather just one
        # so we create one variable to store it and act as return value of this method (answer)
        self.res = 0 # a global variable to provide local access

        # second: recursion
        # recursion only focuses on current node, so we need to know what is input, what is output
        # input is clear, current node, output is harder
        # output != longest path through current node, but rather
        # output == longest leg to pass to parent node
        def depth(node):
            # for current node, we have 3 cases: node is None, node is leaf, node is non-leaf

            # None gets 0: longest leg is 0
            if not node: return 0
            
            # leaf and non-leaf are treated the same
            # we first calculate path and update global longest path
            # we don't know how leg is calculated yet, it's pending implementation
            # but we know return value IS the leg and we just use it
            left = depth(node.left)
            right = depth(node.right) # get the legs
            self.res = max(self.res, left+right) # update the path
            # then we implement leg calculation
            # the following line does 2 things:
            # 1. leg calculation implementation
                # implementation is combined with `if not root: return 0` together
                # None gets 0 as leg, leaf and non-leaf get 1 + child node leg
            # 2. return value for current method
            return 1 + max(left, right) # return the longest leg

        depth(root)
        return self.res


# helper method style
class Solution:
    ans = 0 # fun way to declear global variable
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.ans

    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.ans = max(self.ans, left+right)
        return max(left,right)+1