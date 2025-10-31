class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        def is_valid(array):
            seen = set()
            for num in array:
                seen.add(num)
            if len(seen) == n:
                return True
            return False
        
        for i in range(n):
            row = matrix[i]
            col = [matrix[j][i] for j in range(n)]

            if not is_valid(row) or not is_valid(col):
                return False
        
        return True