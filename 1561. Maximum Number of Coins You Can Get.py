# for each round we pick the smallest number, the largest, and second largest number
class Solution:
    def maxCoins(self, A: List[int]) -> int:
        return sum(sorted(A)[len(A) // 3::2])