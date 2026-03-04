# brute force
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                curr = matrix[r][c]
                if curr == min(matrix[r]) == max(matrix[r][c] for r in range(row)):
                    return [curr]

        return []


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        # 1. Get the minimum of every row
        # matrix[r] is already a list, so min(row) is fast
        row_mins = {min(row) for row in matrix}
        
        # 2. Get the maximum of every column
        # zip(*matrix) is a Python trick to transpose rows into columns
        col_maxs = {max(col) for col in zip(*matrix)}
        
        # 3. The intersection of these two sets gives the lucky numbers
        # Use list() because the problem asks for a list return
        return list(row_mins & col_maxs)