# TLE
class Solution:
    def countPairs(self, d: List[int]) -> int:
        # powers of 2 in binary:
        # 1      -> 1
        # 2      -> 10
        # 4      -> 100
        # 8      -> 1000
        # 16     -> 10000
        # every number has exactly one bit set to 1
        # subtracting 1 flips all bits after that 1
        # for example 8 - 1 = 7
        # 7      -> 0111
        # so 8 & 7 = 0
        def is_power_of_two(n):
            return n > 0 and (n & (n-1)) == 0
        
        count = 0
        for i in range(len(d)-1):
            for j in range(i+1, len(d)):
                if is_power_of_two(d[i]+d[j]):
                    count += 1
        return count


# same logic as 2sum
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter() # hashmap for quick lookup
        res = 0
        max_sum = max(deliciousness) * 2

        for x in deliciousness:
            power = 1
            while power <= max_sum:
                res += count[power - x]
                power <<= 1  # next power of two
            count[x] += 1
        
        return res % (10**9 + 7)
