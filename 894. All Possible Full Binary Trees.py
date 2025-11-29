# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # Full binary trees only exist for odd n
        if n % 2 == 0:
            return []
 
        # use a hsahmap to prevent repeatitive computation
        # key: number of nodes, value: list of all possible trees
        memo = {1: [TreeNode(0)]} # base case: 1 node, 1 possible tree

        # dfs
        def build(count):
            # if trees are pre computated, fetch the list
            if count in memo:
                return memo[count]

            # create a new list
            trees = []

            # for all possible number of nodes in the left subtree
            # Only odd numbers are possible
            for left_count in range(1, count, 2):
                right_count = count - 1 - left_count

                # recursively build left and right subtree
                left_trees = build(left_count)
                right_trees = build(right_count)

                # Combine each left subtree with each right subtree
                for L in left_trees:
                    for R in right_trees:
                        root = TreeNode(0)
                        root.left = L
                        root.right = R
                        trees.append(root)

            # update hashmap
            memo[count] = trees
            return trees

        return build(n)
