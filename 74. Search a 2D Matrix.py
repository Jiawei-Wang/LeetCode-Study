class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        end = rows*cols-1
        while start <= end:
            mid = (start+end) // 2
            if matrix[mid//cols][mid%cols] == target: return True
            if matrix[mid//cols][mid%cols] < target:
                start = mid + 1
            else:
                end = mid -1
        return False
