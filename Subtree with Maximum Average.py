"""
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. 
The average value of a subtree is the sum of its values, divided by the number of nodes.

Example:

Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []
        
# DFS
class Solution: 
    def MaxAverageSubtree(self, root):
        # 必须至少有一个父节点
        if not root or not root.children:
            return None
        
        self.res = [float('-inf'), 0] # self.res[0]: average; self.res[1]: number of nodes
        self.dfs(root)
        return self.res[1]
    
    # input: 当前节点, output: 当前节点对应子树的[总和, 节点总数]
    def dfs(self, root):
        if not root.children:
            return [root.val, 1]
        
        temp_sum, temp_num = root.val, 1
        for child in root.children:
            child_sum, child_num = self.dfs(child)
            temp_sum += child_sum
            temp_num += child_num
            
        if temp_sum/temp_num > self.res[0]:
            self.res = [temp_sum/temp_num, root.val]
        
        return [temp_sum, temp_num]