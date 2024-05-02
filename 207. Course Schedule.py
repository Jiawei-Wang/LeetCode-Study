# 先用prerequisite做一个adjacency list，key=课程编号，value=list of 前置课程
# 将value为空的课程找出来，然后寻找以它为前置课程的其他课程，从value中删去
# 重复直至无法再删去，查看是否每个课程value都为空
# time n^3: 对于一个没有前置课程的课程A，查询其他所有课程，如果A在value中，则删去，三个循环
# space n: 需要一个adj list，以及一个queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 先制作adj list
        adj = dict()
        for i in prerequisites:
            adj[i[0]] = adj.get(i[0], []) + [i[1]]
            adj[i[1]] = adj.get(i[1], [])
            
        # 第一遍先找出没有value的课程
        alreadyMet = True
        start = deque()
        for key in adj:
            if not adj[key]:
                start.append(key)
            else:
                alreadyMet = False
        if alreadyMet:
            return True
        
        # 再进去将start中的课程从其他课程的value中删去，如果任何一个课程value变成空，则将其也加入start
        while start:
            cur = start.popleft()
            for key in adj:
                if cur in adj[key]:
                    adj[key].remove(cur) # pop使用下标，remove使用值
                    if not adj[key]:
                        start.append(key)
                        
        # return not adj: 此语法错误，not dictionary检查的是dictionary中是否还有key
        for i in adj:
            if adj[i]:
                return False
        return True


# 在上一个答案的基础上修改，添加一个set用来保存遍历过的元素
# 此答案不去逐个删减value，而是直接使用dfs查看这个树里是否有cycle的存在
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 先创建adj list
        # 课程编号固定，所以可以直接初始化
        preMap = { i:[] for i in range(numCourses)} 
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()
        
        def dfs(crs):
            if crs in visiting: # 有环
                return False
            if preMap[crs] == []: # 走到头
                return True
            
            visiting.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): return False
                
            # 所有前置课程都返回True，说明此课程可被完成
            visiting.remove(crs) # dfs结束时把之前遍历过的元素逐个删去
            preMap[crs] = [] # 我们已知此课程可被完成，所以前置课程list直接删去
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True


# check if the graph has a cycle
# 1. if node v has not been visited, then mark it as 0.
# 2. if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a ring.
# 3. if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] # 2d list, index = course number, element = prerequisites for course number
        visit = [0 for _ in range(numCourses)] # no element is visited in the beginning
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if visit[i] == -1: # 如果已在当前recursion中，则存在cycle
                return False
            if visit[i] == 1: # 如果已经被检查过，说明没有通过它的cycle
                return True
            visit[i] = -1 # 第一次被visit，将其状态保存
            for j in graph[i]:
                if not dfs(j): 
                    return False # 此recursion中任意一个失败则全部失败
            visit[i] = 1 # 标记为已经visited
            return True # 不存在cycle，返回True
        
        for i in range(numCourses): # 对于任何一个元素都不能有经过它的cycle
            if not dfs(i):
                return False
        return True