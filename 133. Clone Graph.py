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


