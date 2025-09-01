"""
Bézout's identity (also called Bézout's lemma) is a theorem in the elementary theory of numbers:

let a and b be nonzero integers and let d be their greatest common divisor. 
Then there exist integers x and y such that ax+by=d

In addition, the greatest common divisor d is the smallest positive integer that can be written as ax + by

every integer of the form ax + by is a multiple of the greatest common divisor d.
"""
# check if z is a multiple of GCD(x, y)
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            while b:
                temp = b
                b = a % b
                a = temp
            return a
        
        if x + y < z: # we can hold at most x + y gallons
            return False
        if x == z or y == z or x + y == z:
            return True
        return z % gcd(x, y) == 0
        