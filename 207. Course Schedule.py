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