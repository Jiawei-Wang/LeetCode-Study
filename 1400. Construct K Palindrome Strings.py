class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        length = len(s)
        
        if k > length: # we can't find a way to divide length chars into k groups
            return False
        elif k == length: # just put each char into its own group
            return True
        
        # count odds and evens
        # if we have a letters with odd number of occurrence
        # and b letters with even number of occurrence
        # then the least amount of palindromes we need is max(1, odd)
        # example: leet
        # 1 l, 2 e, 1 t, then we need at least 2 palindromes
        count = [0] * 26
        for char in s:
            count[ord(char)-ord("a")] += 1
        odd = 0
        for c in count:
            if c % 2: 
                odd += 1
        
        least = max(1, odd)
        return k >= least
