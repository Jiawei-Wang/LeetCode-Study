'''
读题想法：找环，然后和minimum height tree一样，从外围删除元素
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
'''
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
                
        # 一直删到不能删为止
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
            # 下面这段有bug：找出一个课程A后立刻修改它的后置课程[B,c,D]中的前置课程set，最后再加入cur set，
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


# 这个答案不是很懂，需要再回顾
# 同时这道题还有一个Topological Sort答案，TODO
# DFS
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 首先还是做adj list
        self.graph = collections.defaultdict(list)
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        
        self.res = [] # 答案初始化为空
        
        self.visited = [0 for x in range(numCourses)] # DAG detection 
        for x in range(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
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