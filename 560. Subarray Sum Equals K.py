class Solution:
    def subarraySum(self, A, K):
        # 一个dictionary，里面是每个元素和它出现次数的键值对，当前为空
        # count[V]: the number of previous prefix sums with value V. If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer
        count = collections.Counter()

        count[0] = 1
        ans = 0
        total = 0
        for x in A:
            total += x
            ans += count[total-K]
            count[total] += 1
        return ans
