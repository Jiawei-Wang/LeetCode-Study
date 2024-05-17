# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# same logic as 96. Unique Binary Search Trees
# but instead of returning total number of combinations, we have to return all combinations
# we pick i as root, then we solve the subquestion for [1, i-1] and [i+1, n]
# do it for every i
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate_subtrees(1, n)

    # return a list of all possible trees built from range [s, e]
    # so the list can be used to build bigger trees
    def generate_subtrees(self, s: int, e: int) -> List[TreeNode]:
        res = []

        # base case 1: if there is no range, we add None tree node to the list
        if s > e:
            res.append(None)  # empty tree
            return res
        
        # base case 2; if range is 1: left_subtrees and right_subtrees will be [none]
        # so current function will return a list containing only one node with no children
        # for other cases: take the list of nodes and build a bigger list
        for i in range(s, e + 1):
            left_subtrees = self.generate_subtrees(s, i - 1)
            right_subtrees = self.generate_subtrees(i + 1, e)

            # if there are 2 different left subtrees and 3 different right subtrees
            # then we can build 6 different trees 
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res