class Solution:
    def partitionString(self, s: str) -> int:
        current = set()
        count = 1

        for char in s:
            if char in current:
                current = set()
                count += 1
            
            current.add(char)
        
        return count
