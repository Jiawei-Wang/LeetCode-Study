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