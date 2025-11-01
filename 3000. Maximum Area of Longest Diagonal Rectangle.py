class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0

        for rectangle in dimensions:
            length = rectangle[0]
            width = rectangle[1]
            dia_square = length * length + width * width
            if dia_square > max_diagonal:
                max_diagonal = dia_square
                max_area = length * width
            if dia_square == max_diagonal:
                max_area = max(max_area, length * width)
        
        return max_area
        