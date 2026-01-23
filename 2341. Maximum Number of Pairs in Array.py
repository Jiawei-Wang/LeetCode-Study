class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pending = set()
        paird = 0
        for num in nums:
            if num not in pending:
                pending.add(num)
            else:
                pending.remove(num)
                paird += 1
        return [paird, len(pending)]
