# directed graph with edges, return the path of graph traversal using all edges
# 1. that starts from JFK 
# 2. and has the smallest lexical order
# for example to traverse graph: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] from JFK
# to use all 5 edges: 
# we can do ["JFK","SFO","ATL","JFK","ATL","SFO"]
# or ["JFK","ATL","JFK","SFO","ATL","SFO"], and this one has smaller lexical order, so we choose this one
# this is an Eulerian path question
# Eulerian Path: a path in a graph that visits every edge exactly once
# Eulerian Circuit: an Eulerian Path that starts and ends on the same vertex

"""
Greedy DFS
build the route backwards by finding the end node first, deleting the path to this node, and repeating 
time O(V + E), space O(E)

math behind this: 
In Eulerian paths, there must exist a start node (which is JFK in this problem) and a end node.
End node can be start node or another node.
end node is start node if and only if all nodes has even degree.
end node is another node if and only if there is another odd degree node and start node has an odd degree.
so we can find the end node first
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []
        
        # first create an adj list with cities sorted 
        # why sort: because we want to find the first (by lexical order) path that is valid
        # for example if JFK can go to SFO and ATL, we want to try ATL first
        # if JFK -> ATL -> etc is not valid, then we try JFK -> SFO 
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        # then we start dfs from JFK 
        def dfs(src):
            if adj[src]: # if we can still go somewhere else from src
                while adj[src]: # then we pick the next stop one by one
                    dest = adj[src][0]
                    adj[src].pop(0)
                    dfs(dest)
            path.append(src)

        dfs("JFK")
        return path[::-1]

        """
        execution, with A -> B, A -> C, C -> A as example:
        1. adj list = {A: [B, C], C: [A]}
        2. we start dfs(A), pick B, update adj = {A: [C], C: [A]}, dfs(B)
        3. nothing in B, path = [B], return to previous dfs(A)
        4. pick C, update adj = {A: [], C: [A]}, dfs(C)
        5. pick A, update adj = {A: [], C: []}, dfs(A)
        6. nothing in A, path = [B, A], return to previous dfs(C)
        7. nothing in C, path = [B, A, C], return to previous dfs(A)
        8. nothing in A, path = [B, A, C, A], finish 
        """
