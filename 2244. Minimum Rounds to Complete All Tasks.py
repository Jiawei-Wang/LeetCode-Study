class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        ops = 0
        for key, value in freq.items():
            if value < 2:
                return -1
            
            if value % 3 == 0:
                ops += value // 3
            else:
                ops += value // 3 + 1
        return ops 