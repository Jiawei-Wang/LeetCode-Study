"""
in a graph with n vertices marked from 0 to n-1
we have some directed edges 
find if there is a circle on this graph

读题想法：
和minimum height tree一样，从外围删除元素
and at the end check if graph is empty 

这个图里的edge是有向的，举例: [[0,1], [0,2],[1,2]] 虽然是个环（课程0需要1和2，1需要2），但是以 2->1->0的顺序可以完成课程
但是反过来，如果是[[0,1],[1,2],[2,0]]，则无法完成
1. 画图，获得每个node和它的前置课程
2. 找出没有前置课程的node，删除
3. 更新剩余node的前置课程
4. 重复第二步
5. 如果无法全部删除，则False，如果能全部删除，返回删除顺序

思考：
1. adj list中的value可以用set而不是list来提高搜索速度，因为一个课程的前置课程没有顺序之分
2. 可以将后置课程也放入adj list来避免遍历adj list找它们
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        # key：课程, value：一个list，其中两个set，第一个set保存前置课程，第二个set保存后置课程
        # 例子：0: (1,2), (3)    课程0的前置课程为1和2，后置课程为3
        adj = dict()
        for relation in prerequisites:
            adj[relation[0]] = adj.get(relation[0], [set(), set()]) 
            adj[relation[1]] = adj.get(relation[1], [set(), set()])
        for relation in prerequisites:
            adj[relation[0]][0].add(relation[1])
            adj[relation[1]][1].add(relation[0])
            
        # 先把单独的node拿出来（即没有前置课程，也没有后置课程的课）
        ans = []
        for i in range(numCourses):
            if i not in adj:
                ans.append(i)
                
        # then keep removing nodes with no prerequisite from graph
        while True:
            if not adj:
                return ans
            cur = set()
            for key in adj:
                if not adj[key][0]:
                    cur.add(key)
            if not cur:
                break
            for key in cur:
                ans.append(key)
                if adj[key][1]:
                    for laterCourse in adj[key][1]:
                        adj[laterCourse][0].remove(key)
                del adj[key]
            # 下面这段有bug：找出一个课程A后立刻修改它的后置课程[B,C,D]中的前置课程set，最后再加入cur set，
            # 可能会导致遍历到某个它的后置课程B时发现B也没有前置课程，导致B也被加入当前这轮的cur set
            # for key in adj:
            #     # 找出没有前置课程的课
            #     if not adj[key][0]:
            #         cur.add(key)
            #         # update其他课程的edges然后删掉该课程
            #         if adj[key][1]:
            #             for laterCourse in adj[key][1]:
            #                 adj[laterCourse][0].remove(key)
            # if not cur:
            #     break
            # for key in cur:
            #     ans.append(key)
            #     del adj[key] 
        
        return []


# DFS to check if grpah is DAG
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.res = []

        # first create adj list 
        self.graph = collections.defaultdict(list)
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        
        # 0: not visited yet
        # -1: currently being visited
        # 1: already visited and proven to have no circle
        self.visited = [0 for x in range(numCourses)]

        # then check DAG
        for x in range(numCourses):
            if not self.DFS(x):
                return []

        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
            
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True


# Topological Sort
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses, prerequisites):
        if numCourses <= 0:
            return []

        # 1. Init the two HashMaps
        in_degree = {i: 0 for i in range(numCourses)} # A in-degree map, which record each nodes in-degree
        topo_map = defaultdict(list) # A topo-map which record the Node's children
        # in-degree: how many courses to finish before we can finish current course
        # children: list of courses that have current course as prerequisite

        # 2. Build Map
        for cur_course, pre_course in prerequisites:
            topo_map[pre_course].append(cur_course)  # put the child into its parent's list
            in_degree[cur_course] += 1  # increase child inDegree by 1

        # 3. Iterate the inDegree map, find the Node has 0 inDegree. (If none, there must be a circle)
        #    reduce children's inDegree, until all inDegrees are 0
        res = []
        queue = deque([k for k in in_degree if in_degree[k] == 0])
        while queue:
            key = queue.popleft()
            res.append(key)
            for child in topo_map[key]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        # If the result size is less than numCourses, there is a cycle
        if len(res) != numCourses:
            return []

        return res