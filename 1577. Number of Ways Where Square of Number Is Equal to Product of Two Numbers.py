# 读题想法：找到所有的三元组，a*a = b*c，其中b和c来自同一array，a来自另一个

# 暴力解：n^3 （超时）
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0

        for i in range(len(nums1)):
            for x in range(len(nums2)-1):
                for y in range(x+1, len(nums2)):
                    if nums1[i]*nums1[i] == nums2[x]*nums2[y]:
                        count += 1

        for i in range(len(nums2)):
            for x in range(len(nums1)-1):
                for y in range(x+1, len(nums1)):
                    if nums2[i]*nums2[i] == nums1[x]*nums1[y]:
                        count += 1

        return count


# 解法2: 使用dictionary将复杂度降为 n^2
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # d1和d2分别是nums1和nums2中所有的unique的平方的值和它们的出现次数
        # Time: n
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for i in nums1:
            d1[i * i] += 1
        for i in nums2:
            d2[i * i] += 1

        res = 0

        # 对于nums1中所有的二元组,找出它们的乘积在num2中对应几个平方的值
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                p = nums1[i] * nums1[j]
                if p in d2:
                    res += d2[p]
        # 对num2做同样的事
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                p = nums2[i] * nums2[j]
                if p in d1:
                    res += d1[p]

        return res


# 2025
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Build a frequency dictionary
        def freq(arr):
            mp = {}
            for x in arr:
                mp[x] = mp.get(x, 0) + 1
            return mp

        freq1 = freq(nums1)
        freq2 = freq(nums2)
        
        ans = 0

        # Given target = x^2, count number of (a, b) from freq map where a * b == target
        def count_pairs(freq_map, target):
            total = 0
            for a in freq_map:
                if target % a != 0:
                    continue

                b = target // a
                if b not in freq_map:
                    continue

                # Case 1: distinct a and b → freq[a] * freq[b]
                if a < b:
                    total += freq_map[a] * freq_map[b]

                # Case 2: a == b → combinations C(n, 2) = n*(n-1)//2
                elif a == b:
                    n = freq_map[a]
                    total += n * (n - 1) // 2

            return total
        
        
        # Count nums1[i]^2 == nums2[j] * nums2[k]
        for x in freq1:
            target = x * x
            ans += freq1[x] * count_pairs(freq2, target)
        
        # Count nums2[i]^2 == nums1[j] * nums1[k]
        for x in freq2:
            target = x * x
            ans += freq2[x] * count_pairs(freq1, target)
        
        return ans
