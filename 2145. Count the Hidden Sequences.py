class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        minimum = 0
        maximum = 0

        current = 0
        for num in differences:
            current += num
            minimum = min(minimum, current)
            maximum = max(maximum, current)

        count = max(0, (upper - maximum) - (lower - minimum) + 1)

        return count
        
