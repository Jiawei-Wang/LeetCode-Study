# 给出一个有n个node，n-1个edge的graph，选择任意一个node为root（这个tree不要求是binary tree），找到这棵树的height，返回所有树的最小height
# 读题思考：
# 1. 一棵树中每个node都是相连的，所以不存在走不到某个node的情况
# 2. tree的一个branch的height是：从选定为root的node开始，走到某个只有一个edge的node（此node处于graph的边缘，也就是tree的leaf），所遍历的node数量
# 3. 而整个tree的height是：所有branch的height集合中的最大者
# 4. 所以这道题的答案是以所有的node为root，每个找到所有branch的height，取最大者，然后这一群最大者中取最小者

# brute force：考虑每个node作为root，以及遍历整个tree来获得height
# time O(n^2) 答案正确但超时
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        
        # 先做adj list
        # 注意此list中两个相连的node都互相保存对方信息，所以在BFS时需要防止重复遍历
        adj = dict()
        for edge in edges:
            adj[edge[0]] = adj.get(edge[0], []) + [edge[1]]
            adj[edge[1]] = adj.get(edge[1], []) + [edge[0]]
        
        # 从root开始BFS到leaf，得到路径长度，然后取所有路径中的最长者
        # 将每个node都设为root，找到所有最长路径，然后取其中最短者
        # 题目要求返回所有符合要求的node，即假设有多个最短者，返回这些root
        
        ans = [set() for x in range(n+3)] # index: height, element: a list of nodes (the trees using these nodes as roots have this height)
        
        def helper(root, cur, height, visited, maxHeight):
            # prev：上一层的parent（传递此参数用于防止BFS走回头路）
            # node：当前这层的node
            # height：到这个node时的height（题目要求返回node，不要求返回node的height，所以记录相对大小即可，root的height为0还是1，leaf node返回0还是1，这些不重要）
            
            '''
            adj list没有问题，举例：edges = [[1,0],[1,2],[1,3]]
            那么adj list = {1: [0, 2, 3], 0: [1], 2: [1], 3: [1]}
            但是用于检测是否走到leaf node的原始代码有逻辑问题：
            if len(adj[cur]) == 1:
                ans[height] += [root]
                return
            此代码最后会返回每个node，且部分node重复出现多次  
            debug:
            1. 将ans中的每个元素从list改为set
            2. 修改检测leaf node的代码，添加一个visited set
            3. 对于一个node，只记录其最大值
            '''
            # 如果走到从root走到leaf node，则将root和它的height记录进ans中
            visited.add(cur)
            if len(adj[cur]) == 1 and adj[cur][0] in visited:
                return height
            
            for nextNode in adj[cur]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    maxHeight = max(maxHeight, helper(root, nextNode, height+1, visited, maxHeight))
            return maxHeight
        
        for i in range(n):
            # 找到以 i 为root的tree的height
            maxHeight = helper(i, i, 0, set(), 0)
            ans[maxHeight].add(i)
        
        for i in range(len(ans)):
            if ans[i]:
                return ans[i]


# 从外缘开始向内BFS，第一轮将edge数为1的node删去，第二轮将这些node的邻居删去，etc
# 最后会剩下1或者2个node，它们总是在graph最长的那条路径上靠近中心的位置
# time n space n
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0] 
        
        # 先创建adj list
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        # 找到所有起始的leaf node
        leaves = [i for i in range(n) if len(adj[i]) == 1]

        # 当还剩多于2个node时，我们就继续删减
        while n > 2:
            # 将leaf node删去
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop() # 将leaf node的邻居找出来
                adj[j].remove(i) # 邻居的adj list中将刚才删掉的leaf node的edge给删去
                if len(adj[j]) == 1: newLeaves.append(j) # 然后判断这群邻居中哪些变成了新的leaf node（更新后的edge数为1）
            leaves = newLeaves # 将新的leaf node放入，然后重复
        
        return leaves

