# n
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        return letters[0]
    

# binary search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = low + (high-low)//2
            
            if target >= letters[mid]: 
                low = mid+1
            else:
                high = mid-1
                
        return letters[low]