class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # a + rev(b) == rev(a) + b
        # is equal to
        # a - rev(a) == b - rev(b)
        hashmap = defaultdict(int) # key: num - rev(num), value: number of appearances 
        result = 0
        for num in nums:
            rev = int(str(num)[::-1])
            diff = num - rev
            result += hashmap[diff] 
            result %= (10**9+7)
            hashmap[diff] += 1
        return result