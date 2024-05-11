"""
Minimum Spanning Tree:
1. Prim
2. Kruskal


Prim: 

Purpose: find minimum spanning tree
Type: MST problem
Graph: both negative and non-negative weight, only undirected graph
Data structure: priority queue/min heap
Algorithm: greedy
Time: O(V^2) or O(E log V)
Space: O(V)

1. start with an empty visited list
2. pick an arbitrary node
3. choose the smallest edge connecting it with an unvisited node
4. now we have two nodes in visited list, pick the smallest edge connecting any of the two nodes with an univisted node
5. repeat (pick smallest edge connecting an unvisited node to the group)

for example:
    A - B: 2
    A - C: 3
    A - D: 3
    B - C: 4
    B - E: 3
    C - E: 1
    C - F: 6
    D - F: 7
    E - F: 8
    F - G: 9

1. pick A (or any other node)
2. A-B is the shortest, choose it
3. A-D, A-C, B-E all are 3, pick A-C (or any other one)
4. pick C-E
5. pick A-D
6. B-E is the shortest, however both B and E are visited, so we pick C-F
7. only F-G left, so pick F-G
8. all nodes are in visited list


Kruskal:

Purpose: find minimum spanning tree
Type: MST problem
Graph: both negative and non-negative weight, only undirected graph
Data structure: Union-Find
Algorithm: greedy
Time: O(E log E) or O(E log V)
Space: O(V)

1. pick smallest edge
2. pick second smallest edge (they may form two trees, which is ok)
3. continue to pick in this way (as long as the two nodes are not in the same tree)
(otherwise there will be a cycle and this edge is redundent)

for example:
    A - B: 2
    A - C: 3
    A - D: 3
    B - C: 4
    B - E: 3
    C - E: 1
    C - D: 5
    D - F: 7
    E - F: 8
    F - G: 9
    
1. pick shortest: C-E
2. pick A-B: now we have two trees
3. pick A-D (B-E and A-C are also ok)
4. pick A-C: now we have only one tree
5. pick D-F (B-E is the smallest however B and E are already in one tree)
6. pick F-G
"""