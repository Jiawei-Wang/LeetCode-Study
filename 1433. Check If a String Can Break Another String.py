class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        t1 = sorted(s1)
        t2 = sorted(s2)

        small = min(t1, t2)
        big = max(t1, t2)

        for i in range(len(small)):
            if big[i] < small[i]:
                return False
        return True