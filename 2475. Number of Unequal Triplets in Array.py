class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        candidates = [(key, value) for key, value in hashmap.items()]
        candidates.sort()
        answer = 0
        for i in range(len(candidates)-2):
            for j in range(i+1, len(candidates)-1):
                for k in range(j+1, len(candidates)):
                    answer += candidates[i][1] * candidates[j][1] * candidates[k][1]
        return answer


"""
First, we count numbers using a hash map m.

For numbers a, b and c, we can form m[a] * m[b] * m[c] unique triplets.

Say we have 26 numbers (a...z). Number n forms these number of triplets:

m[a] * m[n] * m[o] + ... + m[a] * m[n] * m[z] +
m[b] * m[n] * m[o] + ... + m[b] * m[n] * m[z] +
...
m[m] * m[n] * m[o] + ... + m[m] * m[n] * m[z].
This formula can be simplified as sum(m[a]...m[m]) * m[n] * sum(m[o]...m[z]).

We can track sum on the left and right of m[n] as we go.

What about 0 <= i < j < k condition? Actually, the relation does not matter.
What matters is that [i, j, k], [i, k, j], [k, i, j] and [k, j, i] represent the same triplet, so it should only be counted once.
"""
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = Counter(nums)
        values = list(freq.values())  # order doesn't matter
        
        ans = 0
        right_sum = sum(values)
        left_sum = 0
        
        for x in values:
            right_sum -= x            
            ans += left_sum * x * right_sum
            left_sum += x
        
        return ans
