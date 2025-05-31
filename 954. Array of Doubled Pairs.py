# see if we can re-order arr so that it looks like [a, 2a, b, 2b, c, 2c, etc]
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = collections.Counter(A)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True