class Solution:
    def hasSameDigits(self, s: str) -> bool:
        curr = [int(char) for char in s]
        while len(curr) > 2:
            nxt = []
            for i in range(len(curr)-1):
                digit = (curr[i] + curr[i+1]) % 10 
                nxt.append(digit)
            curr = nxt
        return curr[0] == curr[1]

        