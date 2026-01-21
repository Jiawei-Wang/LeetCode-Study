class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])

        global_index = 0 # if no row has any zero, first row is picked
        global_count = 0
        
        for r in range(row):
            curr_row = mat[r]
            count = 0
            for c in range(col):
                if curr_row[c] == 1:
                    count += 1
            if count > global_count:
                global_count = count
                global_index = r

        return [global_index, global_count]

                