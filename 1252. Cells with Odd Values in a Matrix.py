"""
bitwise XOR
# True ^ True   = False
# False ^ False = False
# True ^ False  = True
# False ^ True  = True
""" 
# time: m*n+len(indices)
# space: m+n
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # count row and columns that appear odd times
        odd_rows, odd_cols = [False] * m, [False] * n
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True

        # cell (i, j) with odd times count of row + column would get odd values
        return sum(ro ^ cl for ro in odd_rows for cl in odd_cols)
    

# math
# time: m+n+len(indices)
# space: m+n
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_rows, odd_cols = [False] * m, [False] * n
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        return (n - sum(odd_cols)) * sum(odd_rows) + (m - sum(odd_rows))* sum(odd_cols)