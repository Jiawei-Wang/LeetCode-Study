from collections import defaultdict

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        freq = defaultdict(int)

        for num in nums:
            ln = len(num)

            # Case 1: num is prefix of target → looking for suffix
            if target.startswith(num):
                suffix = target[ln:]
                count += freq[suffix]

            # Case 2: num is suffix of target → looking for prefix
            if target.endswith(num):
                prefix = target[:-ln]
                count += freq[prefix]

            freq[num] += 1

        return count
