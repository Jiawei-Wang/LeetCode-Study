# 暴力解: nlogn
# nums1 = sorted(nums1+nums2)
# l = len(nums1)
# if l % 2:
#     return nums1[l//2]
# else:
#     return (nums1[l//2]+nums1[l//2-1])/2

# two pointers: n
# num = []
# l = r = 0
# while l < len(nums1) and r < len(nums2):
#     if nums1[l] < nums2[r]:
#         num.append(nums1[l])
#         l += 1
#     else:
#         num.append(nums2[r])
#         r += 1
# if l < len(nums1):
#     for x in nums1[l:]:
#         num.append(x)
# else:
#     for y in nums2[r:]:
#         num.append(y)
# return num[len(num)//2] if len(num) % 2 else (num[len(num)//2]+num[len(num)//2-1])/2

# 最优解: log(n)
# https://www.youtube.com/watch?v=LPFhl65R7ww&ab_channel=TusharRoy-CodingMadeSimple
class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
        