# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

# 遍历每个node，在每个node都进行dfs找到以它为出发点的全部路径中符合要求的部分
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths
    
    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return 
        # dfs break down 
        self.test(node, target) # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
            
        # test break down
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)


# brute force but with cache
# 上一次是以每个node为起始点，往下找符合要求的路径，外层dfs获得node，内层dfs计算路径
# 这次是以root为起始点，记录其与每个node之间的路径，然后通过 root~b - root~a 的方式计算 a~b 的路径，一层dfs即可
# we traverse through the tree, at each node, we can get the currPathSum (from root to current node). 
# If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1} # 初始化的意思是：如果currPathSum - target = 0，返回1
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1 # 一条路径，只有它和它下面的子路径可以用，recursion回到此层时就标记为-1，这样下次遇到时+1正好为0