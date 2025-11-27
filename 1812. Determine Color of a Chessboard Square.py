class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char = coordinates[0]
        integer = int(coordinates[1])

        char_diff = ord(char) - ord("a")
        if char_diff % 2 == 1:
            color = True
        else:
            color = False

        int_diff = integer - 1
        if int_diff % 2 == 1:
            color = not color
        
        return color