class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        blocks = set()
        for guard in guards:
            blocks.add((guard[0], guard[1]))
        for wall in walls:
            blocks.add((wall[0], wall[1]))

        visited = set()

        def travel(guard):
            row_up = guard[0] - 1
            row_down = guard[0] + 1
            col_left = guard[1] - 1
            col_right = guard[1] + 1
        
            while row_up >= 0: 
                curr = (row_up, guard[1])
                if curr not in blocks:
                    visited.add(curr)
                    row_up -= 1
                else:
                    break
            
            while row_down < m:
                curr = (row_down, guard[1])
                if curr not in blocks:
                    visited.add(curr)
                    row_down += 1
                else:
                    break
            
            while col_left >= 0 :
                curr = (guard[0], col_left)
                if curr not in blocks:
                    visited.add(curr)
                    col_left -= 1
                else:
                    break
            
            while col_right < n:
                curr = (guard[0], col_right)
                if curr not in blocks:
                    visited.add(curr)
                    col_right += 1
                else:
                    break
            
        
        total = 0
        for guard in guards:
            travel(guard)
        return m * n - len(guards) - len(walls) - len(visited)



