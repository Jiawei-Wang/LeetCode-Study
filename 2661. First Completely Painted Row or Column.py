class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        value_to_index = dict()
        row_hashmap = defaultdict(set)
        col_hashmap = defaultdict(set)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                value_to_index[mat[i][j]] = (i, j)
                row_hashmap[i].add(j)
                col_hashmap[j].add(i)
        
        for index in range(len(arr)):
            i, j = value_to_index[arr[index]]
            row_hashmap[i].remove(j)
            col_hashmap[j].remove(i)
            if len(row_hashmap[i]) == 0 or len(col_hashmap[j]) == 0:
                return index
        

        

