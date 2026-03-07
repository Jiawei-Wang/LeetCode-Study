class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort(reverse=True)
        
        index = 0
        while total_apple > 0:
            total_apple -= capacity[index]
            index += 1
        
        return index