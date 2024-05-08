"""
Shortest path finding: 
1. Dijkstra
2. Bellman-Ford
negative weight: Bellman-Ford works, Dijkstra fails 
(because Dijkstra is greedy, for example it thinks 
one step path s -> 3 -> e is shorter than two step path s -> 4 -> m -> -2 -> e)
negative cycles: both fail (shortest path doesn't exist)


1. Dijkstra: 

Purpose: find shortest path from one node to every other node
Type: single source shortest path problem
Graph: both undirected and directed graph, only non-negative weight 
Data structure: priority queue/min heap
Algorithm: greedy
Time: O((V + E) log V)
Space: O(V)

1. every node is unvisited at first
2. start from one node, distance to itself is 0, all other nodes are +inf distance
3. visit all its neighbor nodes, update their distance using edge weight
4. mark first node as visited, pick the smallest distance node in unvisited list as next to visit
5. start from this node, visit all its neighbor nodes an update their distance
6. mark this node as visited and pick the smallest istance node in unvisited list as next to visit
7. start from this node and repeat

for example: 
    5 nodes: A, B, C, D, E in a weighted and directed graph: 
    A -> B: 4
    A -> C: 2
    B -> C: 3
    C -> B: 1 
    B -> D: 2
    C -> D: 4
    B -> E: 3
    C -> E: 5
    E -> D: 1

1. pick starting node: A
    A: 0
    B to E: +inf
    all nodes are in unvisited list: [A, B, C, D, E]
2. update neighbor distance: B and C are reachable from A: 
    A: 0
    B: 4
    C: 2
    D and E: +inf
    A is taken from unvisited list
3. pick smallest from unvisited list: C, and update neighbor distance:
    A: 0
    B: 3 (updated from 4)
    C: 2
    D: 6
    E: 7
    C is taken from unvisited list
4. then do the same for B:
    A: 0
    B: 3
    C: 2
    D: 5
    E: 6
5. then D:
    no update
6. then E:
    no update
7. after all nodes are visited, final distance from A is:
    A: 0
    B: 3
    C: 2
    D: 5
    E: 6 


2. Bellman-Ford:

Purpose: shortest path from one node to every other node
Type: single source shortest path problem
Graph: both undirected graph (non-negative weight) and directed graph (negative and non-negative weight)
Data structure: N/A
Algorithm: DP
Time: O(VE)
Space: O(V)

1. repeat at most V-1 times (V-1 iterations)
2. each time visit all nodes and update all distance
3. no unvisited list, all nodes are visited once every time (order doesn't matter)

for example: 
    6 nodes: S, A, B, C, D, E in a weighted and directed graph: 
    S -> A: 10
    S -> E: 8
    E -> D: 1
    D -> C: -1
    C -> B: -2
    B -> A: 1
    D -> A: -4
    A -> C: 2
    so at most 6-1=5 iterations

1. first iteration:
    1. pick s as starting point
        S: 0
        all others: +inf
    2. update s neighbor
        S: 0
        A: 19
        B/C/D: +inf
        E: 8
    3. pick A:
        S: 10
        A: 10
        B: +inf
        C: 12
        D: +inf
        E: 8
    4. pick B, B is +inf right now so we skip B
    5. pick C:
        S: 0
        A: 10
        B: 10
        C: 12
        D: +inf
        E: 8
    6. pick D, D is +inf right now so we skip D
    7. pick E: 
        S: 0
        A: 10
        B: 10
        C: 12
        D: 9
        E: 8
2. second iteration: 
    we go through all nodex again: S, A, B, C, D, E, this time only visiting D can update the distance
    S, A, B, C, E visits are skipped
        S: 0
        A: 5
        B: 10
        C: 8
        D: 9
        E: 8
3. third iteration: some changes as well
4. fourth iteration: no change at all (we finish and no more iteration)
"""


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


