class Solution:
    def binaryGap(self, n: int) -> int:
        string = bin(n)[2:]
        lead = -1
        gap = 0
        for index in range(len(string)):
            if string[index] == "1":
                if lead != -1:
                    gap = max(gap, index - lead)
                lead = index
        return gap