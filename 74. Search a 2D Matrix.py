class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search + n*m extra space
        nums = []
        for i in matrix:
            nums += i
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return True
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1 extra space: basically just calculate the [i, j] instead of making a new list
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