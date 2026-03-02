"""
treat it like a binary tree
start from row 1 col 1 (root): 0
for row 2: 
    col 1 is left child of 0: 0
    col 2 is right child of 0: 1
for every row below:
    left child is the same value as parent
    right child is flip: 0 -> 1 or 1 -> 0
so for row x col y: 
    if y is even: 
        it is the right child of row x-1 col y//2: flip value
    if y is odd:
        it is the left child of row x-1 col (y+1)//2: same value
"""
class Solution:
    def kthGrammar(self, row: int, col: int) -> int:
        flip = False
        while row != 1:
            if col % 2 == 0:
                flip = not flip
                col //= 2 
            else:
                col = (col+1) // 2
            row -= 1
        return 1 if flip else 0
