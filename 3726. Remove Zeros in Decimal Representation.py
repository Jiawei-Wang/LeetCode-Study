class Solution:
    def removeZeros(self, n: int) -> int:
        string = str(n)
        array = []
        for char in string:
            if char != "0":
                array.append(char)
        return int("".join(array))
