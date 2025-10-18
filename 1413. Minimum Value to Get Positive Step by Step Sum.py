class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        smallest = float("inf")
        for num in nums:
            total += num
            smallest = min(smallest, total)
        return max(-smallest+1, 1)

        