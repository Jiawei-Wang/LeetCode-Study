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
