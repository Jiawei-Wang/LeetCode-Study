# we don't know what shift generates the biggest overlapping
# so we try every possible shift (map every 1 in A to every 1 in B)
# and the tricky part is, instead of doing every shift and calculating the overlapping each time
# we do it on the fly by using a hashmap
class Solution:
    def largestOverlap(self, A, B):
        n = len(A)
        
        A_ones = []
        B_ones = []
        
        # Collect coordinates of 1s
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    A_ones.append((i, j))
                if B[i][j] == 1:
                    B_ones.append((i, j))
        
        shift_count = {}
        max_overlap = 0
        
        # Count shifts needed to align 1s
        for ax, ay in A_ones:
            for bx, by in B_ones:
                # for all possible shifts
                dx = bx - ax
                dy = by - ay
                shift = (dx, dy) 
                
                shift_count[shift] = shift_count.get(shift, 0) + 1
                max_overlap = max(max_overlap, shift_count[shift])
        
        return max_overlap
