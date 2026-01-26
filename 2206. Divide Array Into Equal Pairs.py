class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        for key, value in counter.items():
            if value % 2:
                return False
        return True