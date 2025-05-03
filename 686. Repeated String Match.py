# check if b exists in an infinite loop of a 
# m*n
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)

        # we don't know which char in a will b start with
        # so we try each one
        for i in range(len_a):
            j = 0
            while j < len_b and a[(i + j) % len_a] == b[j]:
                j += 1
            if j == len_b: # if we can move to the end of b by starting from this char
                return (i + j - 1) // len_a + 1

        return -1
    

# KMP
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Build the prefix table for KMP
        prefTable = [0] * (len(b) + 1)  # 1-based indexing
        sp, pp = 1, 0
        while sp < len(b):
            if b[pp] == b[sp] or pp == 0:
                if b[pp] == b[sp]:
                    pp += 1
                else:
                    pp = 0
                sp += 1
                prefTable[sp] = pp
            else:
                pp = prefTable[pp]

        # Match b inside repeated a using KMP-like logic
        i, j = 0, 0
        while i < len(a):
            while j < len(b) and a[(i + j) % len(a)] == b[j]:
                j += 1
            if j == len(b):
                return (i + j - 1) // len(a) + 1
            j = prefTable[j]
            i += max(1, j - prefTable[j])

        return -1
