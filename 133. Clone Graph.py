"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        m = dict() # 储存新创建的node
        visited = set() # 储存被遍历过的node的信息
        queue = collections.deque([node]) # BFS
        
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val) # 创建新的node
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val) # Node class中默认 val = 0, neighbors = None，所以在创建新Node时并不需要初始化neighbors
                m[n].neighbors.append(m[neigh]) # 因为m[n]中储存的是一个Node对象，它有neighbors属性
                queue.append(neigh) 
        return m[node]
    
"""
对解法的理解：
1. 总体思路是BFS找到所有还未被遍历的元素，然后创建一个copy并保存
2. 使用queue来implement BFS，使用hashset保存遍历信息，使用hashmap来保存copy
3. 走到一个新元素时，先检查是否已被遍历过，再创建copy（新的对象），然后使用for循环来：1.创建其邻居的copy，2.将邻居加入其neighbors属性，3.将邻居放入queue
"""


# DFS: 和上一解的区别是使用了deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        m, visited, stack = dict(), set(), deque([node])
        
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                stack.append(neigh)
        return m[node]


# DFS recursively: 不使用额外的stack，因为recursion本身就是stack，但是需要使用helper
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m, visited = dict(), set()
        self.dfs(node, m, visited)
        return m[node]
    
    def dfs(self, n, m, visited):
        if n in visited:
            return 
        visited.add(n)
        if n not in m:
            m[n] = Node(n.val)
        for neigh in n.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
            m[n].neighbors.append(m[neigh])
            self.dfs(neigh, m, visited)


"""
2024
understand the question:
0. we are given one node to start with
1. we need to travel through all current nodes, either BFS or DFS
2. when we visit a new node, we need to build a clone node 
3. both the value and neighbors list need to be built
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""
understand the answer:
1. we need a hashmap for quick lookup, this is to replace the set
2. also we can store new nodes inside the hashmap, so the (set + hashmap) combo is no longer needed
3. when all new nodes are added to hashmap, just return the first node
4. queue is needed for BFS
5. we start from given input node: put it inside queue, create a clone
6. we check its neighbors and do the same thing again for unvisited nodes
7. regardless of visited or not, we add neighbors to the clone's neighbors list
"""
# BFS with 1 hashmap + 1 queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # first, corner case
        if not node:
            return None

        visited = {}  # hashmap to keep all newly created nodes + track visited nodes

        # starting from given input node
        queue = collections.deque([node])  # Queue for BFS traversal
        visited[node] = Node(node.val)  # Clone starting node

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited: # whenever we find a new node
                    queue.append(neighbor)  # Add neighbor to queue for pending visit
                    visited[neighbor] = Node(neighbor.val)  # Clone this node by creating a new one
                    
                visited[current_node].neighbors.append(visited[neighbor]) # build neighbors list for current node

        return visited[node]


"""
change BFS to DFS:
1. still same hashmap for node storage and lookup
2. main method needs to return the first clone node, same as bfs
3. for dfs helper method, it needs to do two things at every stack: 
    1) return the node: either by creating a new one or fetching from hashmap
    2) build the neighbors list <- this is where we enter next stack as well 
4. first we clone the given input node and put it inside hashmap
5. then we append all neighbor nodes into neighbors list
    1) we enter next stack and do the same thing to its neighbor nodes: create or fetch, and build their neighbors list
    2) exit the stack by returning the created/fetched neighbor node
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None  

        visited = {}

        # dfs returns a cloned node
        def dfs(node):
            # return the one from hashmap if it was already cloned in previous visit
            # and we can exit this stack without doing anything else
            if node in visited:
                return visited[node]  

            # for never visited node, clone it, and put it inside hashmap
            copy = Node(node.val) 
            visited[node] = copy  
            
            # then we populate its neighbors list
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))  # dfs next stack will create the node, and return it so it can be added to current node's neighbors list

            # return the newly created one if it is not in hashmap 
            return copy 

        return dfs(node)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {} # key: node, value: new copy of node
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            else:
                copy = Node(node.val)
                old_to_new[node] = copy
                
                for nei in node.neighbors:
                    copy.neighbors.append(clone(nei))
                return copy 
        
        return clone(node) if node else None