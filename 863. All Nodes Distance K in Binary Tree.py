# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 找到距离目标node k个edge的所有node
# 思考：找到目标node后可以bfs找到它下面的node，但是它上面以及旁边的node该怎么找
# 解法：将tree转变为graph然后bfs
class Solution:
    def distanceK(self, root, target, K):
        # 第一步：dfs将tree转变为无向图
        conn = collections.defaultdict(list)
        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            # in-order traversal
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        # the initial parent node of the root is None
        connect(None, root)
        
        # 第二步：bfs找答案
        # start the breadth-first search from the target, hence the starting level is 0
        bfs = [target.val]
        seen = set(bfs)
        # all nodes at (k-1)th level must also be K steps away from the target node
        for i in range(K):
            # expand the list comprehension to strip away the complexity
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
            # add all the values in bfs into seen
            seen |= set(bfs)
        return bfs
