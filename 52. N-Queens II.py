# solution 1: return N-Queens answer
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(locations, xy_dif, xy_sum):
            row = len(locations)
            if row == n:
                result.append(locations)
                return 
            for col in range(n):
                if col not in locations and row-col not in xy_dif and row+col not in xy_sum:
                    dfs(locations+[col], xy_dif+[row-col], xy_sum+[row+col])

        result = []
        dfs([],[],[])
        return len(result)
        

# solution 2: dfs
class Solution:
    def totalNQueens(self, n):
        diag1 = set()
        diag2 = set()
        cols = set()
        
        return self.helper(n, diag1, diag2, cols, 0)

    def helper(self, n, diag1, diag2, cols, row):
        if row == n:
            return 1
        
        solutions = 0
        
        for col in range(n):
            if row + col not in diag1 and row - col not in diag2 and col not in cols:
                    
                diag1.add(row + col)
                diag2.add(row - col)
                cols.add(col)
                
                solutions += self.helper(n, diag1, diag2, cols, row + 1)
            
                diag1.remove(row + col)
                diag2.remove(row - col)
                cols.remove(col)
        
        return solutions