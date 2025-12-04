# ask: can we divide the entire deck into groups of size X where X >= 2 and each group contains only identical values
# insight: let's say we can divide deck into equal groups of size X, then
# for example: value 1 with 8 counts, value 2 with 4 counts and value 3 with 12 counts
# X must be able to divide all the counts
# gcd(8, 4, 12) = 4
# so to make X >= 2, X can be either 4 or 2
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Euclidean GCD algorithm
        # same as: from math import gcd
        def gcd(a, b): 
            while b: 
                a, b = b, a % b
            return a

        from collections import Counter
        count = Counter(deck).values()
        # we only care about counts of each unique card, value of the card doesn't matter
        
        from functools import reduce
        return reduce(gcd, count) > 1 
        # for example: count has 3 elements: [8, 4, 12]
        # then reduce(gcd, count) = gcd(gcd(8, 4), 12)