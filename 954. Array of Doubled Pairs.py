from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        # Sort keys by absolute value
        # This ensures for [4, -2, -4, 2] we look at 2 before 4, and -2 before -4.
        for x in sorted(count.keys(), key=abs): # [4, -2, -4, 2] would be [2, -2, 4, -4]
            # If we've already used all of x, skip it
            if count[x] == 0:
                continue
            
            # If we have N copies of x, we need N copies of 2*x
            if count[x] > count[2 * x]:
                return False
            
            # Subtract the counts
            # If x is 0, this works out correctly as long as count[0] is even
            count[2 * x] -= count[x]
            count[x] = 0
            
        return True