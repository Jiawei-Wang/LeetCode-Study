# BFS
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: 
            return 0
        
        routes = [set(element) for element in routes]  
        
        # 将每个bus视为一个node，key = node，value = 和这个bus拥有共同stop的bus的集合
        graph = collections.defaultdict(set) 
        
        # 将拥有相同stop的bus放入graph中
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        # 找到经过出发点stop的所有bus，找到经过目标点stop的所有bus
        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        # BFS：遍历seen，每次选一个bus然后bfs查看是否能在走完所有邻居前找到目标点stop
        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1