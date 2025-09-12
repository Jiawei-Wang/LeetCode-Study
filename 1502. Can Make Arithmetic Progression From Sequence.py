class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        hashset = set(arr)
        if len(hashset) == 1: # all same number
            return True
        if len(hashset) != len(arr): # at least 2 numbers are the same but not all
            return False

        # find smallest and 2nd smallest
        fir = arr[0]
        sec = float('inf')
        for num in arr[1:]:
            if num < fir:
                sec = fir
                fir = num
            elif num < sec:
                sec = num
        
        # iterate
        gap = sec - fir
        cur = sec
        for i in range(len(hashset)-2):
            cur += gap
            if cur not in hashset:
                return False
        return True