class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        ops = 0
        for key, value in freq.items():
            if value < 2:
                return -1
            
            if value % 3 == 0:
                ops += value // 3
            else:
                ops += value // 3 + 1
                # for example
                # 16 = 3 * 4 + 2 * 2
                # 17 = 3 * 5 + 2 * 1

        return ops 
            