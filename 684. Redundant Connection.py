# we have n nodes labeled from 1 to n with n edges
# so it's a tree with an extra edge
# return the edge that creates the circle
# if there are multiple return the last one in input


# DFS
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.connected = defaultdict(set) # key: the node, value: set of nodes that we alreay know we can reach from this node

        for edge in edges:
            self.visited = defaultdict(bool) # when we use a new edge, we restart the visit, so no node is visited 
            x, y = edge[0], edge[1]
            # if we can already prove y can be connected to x 
            if self.is_already_connected(x, y):
                return edge
            # we know x, y are reachable from each other
            self.connected[x].add(y)
            self.connected[y].add(x)
            
    def is_already_connected(self, x, y):
        if x == y:
            return True
        for reachable in self.connected[x]:
            if not self.visited[reachable]:
                self.visited[reachable] = True
                if self.is_already_connected(reachable, y):
                    return True
        return False


# Union Find
# issue with union-find: tree can be quite deep, worst case is O(n) (tree looks like linked list)
# optimization for union-find: Union by rank
# basic idea: always attach a smaller depth tree under root of the deeper tree
# worst case: O(logn)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * (len(edges) + 1)
        rank = [0] * (len(edges) + 1) # union by rank

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y): # union by rank
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
                rank[root_y] += 1
                return True
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
                return True

        for x, y in edges:
            if not union(x, y): 
                return [x, y]