"""
assume magic square is 
    |  c1  c2  c3
------------------- 
r1  |  a1, a2, a3
r2  |  a4, a5, a6
r3  |  a7, a8, a9

we know they are from 1 to 9
so a1 + a2 + a3 + ... + a9 = 45
in order for each row and each col to have the same sum
they all must be 15

then for a5
r2 a2 + a5 + a8 = 15
c2 a4 + a5 + a6 = 15
d1 a1 + a5 + a9 = 15
d2 a3 + a5 + a7 = 15

so 45 + 3 * a5 = 60
a5 = 5
that means any square must have 5 in the center

for the other 8 blocks:
each opposite pair has sum = 10
for example
a1 + a9 = 10
a4 + a6 = 10
a7 + a3 = 10
therefore the two opposite numbers should be both odd or both even

for three numbers for example a1 + a2 + a3 = 15
there must be either 1 odd number or 3 odd numbers
since we only have 4 odd numbers for all 8 blocks
each row and each col will only get 1 odd number
therefore a2, a4, a6, a8 are odd numbers
and a1, a3, a7, a9 are even numbers

for 4 odd numbers to have two pairs with sum = 10
they have to be 1+9 and 3+7
assuming a2 = 1 
(a4, a6, a8 don't matter since we can rotate the peripheral cycle to make any of them on r1 c2)
then a8 = 9
then a7 + a9 = 15 - 9 = 6
so a7 and a9 must be 2 and 4 (these two even numbers are the only ones sum up to 6)
(which one takes 2 doesn't matter since we can clockwise or anticlockwise the peripheral cycle as well)

then a1 has to be 6 to make a1 + a5 + a9 = 15
then .....

eventually we get the peripheral cycle as [6, 1, 8, 3, 4, 9, 2, 7]
we just need to check both clockwise and anticlockwise
"""
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            s = "".join(str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)

        # check every a1
        return sum(isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if grid[i + 1][j + 1] == 5)