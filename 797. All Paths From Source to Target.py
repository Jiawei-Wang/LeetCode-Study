# dfs
class Solution:
    def allPathsSourceTarget(self, paths: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for city, neighbors in enumerate(paths):
            graph[city] = neighbors

        destination = len(paths) - 1
        all_paths = []
        
        def dfs(city, current_path):
            if city == destination:
                all_paths.append(current_path+[city])
                return
            
            if graph[city]:
                for neighbor in graph[city]:
                    dfs(neighbor, current_path+[city])

        dfs(0, [])        
        return all_paths