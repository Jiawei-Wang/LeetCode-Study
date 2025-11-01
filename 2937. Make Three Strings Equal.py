class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        length = min(len(s1), len(s2), len(s3))
        i = 0
        while i < length and s1[i] == s2[i] == s3[i]:
            i += 1

        # corner case: "a", "b", "c" 
        # since we never entered while loop, i == 0
        if i == 0:
            return -1
        
        # now i stands at the index where everyone's [0:i+1] are the same
        # for example: "a", "ab", "ac", i will be 1
        # this also works on corner case: "aa", "aa", "aa"
        # since i will be 2
        else:
            return len(s1) + len(s2) + len(s3) - i * 3
