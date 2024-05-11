class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        c = collections.defaultdict(list) # key: a node on the graph, value: tuples of all other nodes (distance, node)
        
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        # 初始化
        cnt = 1 # 遍历到第一个点
        ans = 0 # 此时总边长为0
        visited = [0] * n 
        heap = c[0] # heap中有0这个点在dictionary中的value，即所有tuple
        visited[0] = 1 # 第一个点被visited
        heapq.heapify(heap) 
        while heap:
            d, j = heapq.heappop(heap) # 先从距离0最近的邻居开始
            if not visited[j]: 
                visited[j], cnt, ans = 1, cnt+1, ans+d # 将邻居放入visited表，遍历过的node总数+1，且将两者距离加入总边长
                for record in c[j]: heapq.heappush(heap, record) # 将这个邻居的所有邻居信息放入表中
            if cnt >= n: break 
        return ans


# 2024

# Kruskal: build a MST by picking smallest edge each step
# to build the MST: 
# 1. min heap is needed:        to pick the smallest edge
# 2. union find is needed:      to check if the edge is redundant
# (two nodes are in the same union-find group already -> these nodes are on same tree -> edge will create cycle)
# 3. an exit check is needed:   to exit when all points are connected 
class Solution:

    # for 2. union find: we need two things:
    # 2-1 helper function find and union
    # 2-2 a group list
    def find(self, parent, i): # 2-1 find: return the root of group where i is in
        if parent[i] < 0:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        res = 0
        arr = []
        parent = [-1] * length # 2-2 the group list of union find
        # normally we use parent[i] = i to indicate everyone is their own group
        # this one is better because -1 can also be used to calculate group size
        
        # for 1. min heap: we build it first
        for i in range(length):
            for j in range(i + 1, length):
                arr.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        heapq.heapify(arr)

        # now we go into the main part: build MST
        # we check each edge, see if it can be added
        # and we also check when to stop 
        while arr: 
            edge, i, j = heapq.heappop(arr)
            i_root, j_root = self.find(parent, i), self.find(parent, j)

            # if edge creates cycle we just skip this loop
            # if not: since this edge is the optimal edge, we add it
            if i_root != j_root: 
                res += edge

                """
                the following part serves as both 
                2-1 helper function union for union-find
                3. exit check

                root of a group initially is -1 
                when we merge two groups together 
                one root adds the value of another root:
                for example -3 += -1 (a group of size 3 is merged with a group of size 1)
                """
                parent[i_root] += parent[j_root] # i_root still indicates group size
                parent[j_root] = i_root # we let j group merge into i group, now j_root points to i_root
                if parent[i_root] == -length: # after adding the edge, if group size is already length, we can stop 
                    break

        return res


# Prim: pick a node, pick smallest edge, update node group, pick next smallest edge, repeat
# 1. visited list is needed:    to store visited nodes 
# 2. min heap is needed:        to store available edges
# for this question: we also need to contantly calculate and add new edges
import heapq
class Solution:
    def minCostConnectPoints(self, ps: List[List[int]]) -> int:
        n = len(ps)
        res = 0
        visited = [False] * n # no node has been visited
        i = 0 # we pick 0-th node as starting node
        pq = [] # currently we have no available edges in min heap

        # build MST
        for count in range(n-1): # each loop our goal is to add an edge to MST, in total n-1 edges  
            """
            for first loop: 
                1. mark 0-th node as visited
                2. add all its edges to heap (all other nodes can form one edge with it)
                3. pick the smallest edge in heap (guaranteed to not form cycle)
                4. move onto next node
            """

            # for all other loops, extra checks are needed

            visited[i] = True # 1. mark current node as visited

            # 2. add edges to heap 
            for j in range(n): # current node i can be connected to any node j
                # optimization: we only care about j that are not visited yet 
                # if not, i and j will form a redundent edge that will never be used
                # so we don't have to add all edges to heap
                if not visited[j]: 
                    dist = abs(ps[i][0] - ps[j][0]) + abs(ps[i][1] - ps[j][1])
                    heapq.heappush(pq, (dist, j))
            
            # 3. pick next edge 
            # now with all edges at hand, and node group updated, we need to find smallest edge that doesn't form cycle
            while visited[pq[0][1]]: # previously added edge may not be suitable anymore, we remove it
                heapq.heappop(pq) 
            edge = heapq.heappop(pq) # now we have a suitable one 
            res += edge[0]
            i = edge[1]
        
        return res
    