"""
一笔画问题: https://en.wikipedia.org/wiki/Eulerian_path

Eulerian Path: a path in a graph that visits every edge exactly once
Eulerian Circuit: an Eulerian Path that starts and ends on the same vertex

For an undirected graph: 

Eulerian Circuit exists if: 
1. All vertices with non-zero degree are connected. We don’t care about vertices with zero degree 
   because they don’t belong to Eulerian Cycle or Path (we only consider all edges). 
2. All vertices have even degree.

Eulerian Path exists if:
1. Same as condition (1) for Eulerian Cycle.
2. If zero or two vertices have odd degree and all other vertices have even degree. 
   Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)


In-degree: The number of edges directed towards the vertex.
Out-degree: The number of edges directed away from the vertex.

For a directed graph:
1. Strongly Connected: Unlike undirected graphs, all vertices with non-zero degree must belong to a single strongly connected component in the directed graph. 
   This means you can travel from any vertex with non-zero degree to any other vertex with non-zero degree by following directed edges.
2. In-degree and Out-degree: Here's where things differ:
    1) Eulerian Circuit: Every vertex with non-zero degree must have equal in-degree and out-degree. 
                         This ensures you can enter and exit each vertex with the same number of edges while following the closed loop.
    2) Eulerian Path: Two possibilities exist:
        1> No vertex can have a difference between in-degree and out-degree by more than 1. 
           In other words, all vertices must have nearly equal in-degree and out-degree. 
           There can be at most one vertex with in-degree 1 more than its out-degree (source vertex), 
           and at most one vertex with out-degree 1 more than its in-degree (sink vertex). 
           All other non-zero degree vertices must have equal in-degree and out-degree.
        2> The graph cannot have an Eulerian path at all.  
"""