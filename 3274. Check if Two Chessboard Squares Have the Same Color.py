class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def is_black(coordinate):
            letter = coordinate[0]
            number = coordinate[1]
        
            total = ord(letter) - ord("a") + int(number)
            return total % 2
    
        return is_black(coordinate1) == is_black(coordinate2)