# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 从root出发的两条并不一定是最长线路，需要找到每个从每个点出发的线路长度并保留最大值

        self.res = 0 # 学习全局变量在methods中的转移方法

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)

            # 对于一个点，其res为res或左右子树长度之和
            self.res = max(self.res, left+right)

            # 对于一个点而言，只需要保留其较长的那个子树并 +1
            return 1 + max(left, right)

        depth(root)
        return self.res



# 05-13-2022
class Solution:
    ans = 0
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
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0 # global longest path 

        def length(node):
            if not node:
                return 0
            
            left = length(node.left)
            right = length(node.right) # get two legs

            self.answer = max(self.answer, left + right) # update path

            return 1 + max(left, right) # only keep the longest leg for parent node 
        
        # we don't dp: return length(root), since length(root) is just one leg length, not path length
        length(root)
        return self.answer