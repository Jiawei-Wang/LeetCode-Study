class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        best = 0
        for g in gain:
            total += g
            best = max(best, total)
        return best