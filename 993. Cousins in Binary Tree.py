# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # DFS
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # 如果该node值和要找的值相同，返回其深度和parent，不然返回其左右子node
        def dfs(node: TreeNode, parent: TreeNode, depth: int):
            if not node or len(results) == 2:
                return
            else:
                if node.val == x or node.val == y:
                    results.append((parent, depth))
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)

        # 初始化
        results = []
        dfs(root, None, 0)
        
        # 如果二者parent不同但depth相同，返回true
        return results[0][0] != results[1][0] and results[0][1] == results[1][1]

    # BFS
	def isCousins(self, root, x, y):

        # https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
		nodes = collections.defaultdict(list)
		queue = [(root,0,0)]
		while queue:
			node,level,parent = queue.pop(0)
			nodes[node.val] = [level,parent]

			if node.left:
				queue.append((node.left,level+1,node.val))
			if node.right:
				queue.append((node.right,level+1,node.val))

		if nodes[x][0]==nodes[y][0] and nodes[x][1] != nodes[y][1]:
			return True

		return False
