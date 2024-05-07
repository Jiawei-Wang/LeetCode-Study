"""
the median of two sorted arrays will be == (median of array A + median of array B) / 2
only when both arrays have the same length

for example:
A = [1, 3, 5], median 3
B = [2, 4, 5, 8], median 4.5

average median = (3 + 4.5) / 2

true array = [1, 2, 3, 4, 5, 5, 8]
true median = 4
"""


# 暴力解: combine, sort again, then find median, nlogn 
# nums1 = sorted(nums1+nums2)
# l = len(nums1)
# if l % 2:
#     return nums1[l//2]
# else:
#     return (nums1[l//2]+nums1[l//2-1])/2


# two pointers: combine using two pointers, then fin median, n
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


"""
最优解: log(n)
https://www.youtube.com/watch?v=LPFhl65R7ww&ab_channel=TusharRoy-CodingMadeSimple
1. suppose we have A = [a1, a2, a3, a4, a5, a6] and B = [b1, b2, ..., b8]
2. if we cut A into two parts: [a1, a2] and [a3, ..., a6]
3. then in order to keep both sides with same number of elements
4. we will have to cut B into [b1, ..., b5] and [b6, b7, b8] 
5. we already know a2 <= a3 and b5 <= b6
6. so it's only good if a2 <= b6 and b5 <= a3 (all elements in two left halves <= all elements in two right halves)
7. then we just need the four elements for median calculation: median = (max(a2, b5) + min(a3, b6)) / 2

1. so now our job is to find the partition point, use it to divide both A and B, then check for validation
2. for validation: both (max of left A <= min of right B) and (max of left B <= min of right A) have to be true
3. elif (max of left A <= min of right B) is false: max of left A > min of right B: we went too far right on A, the true partition point should be towards left on A
4. elif: (max of left B <= min of right A) is false: we went too far right on B (too far left on A), the true partition point should be towards right on A 
5. there no such thing as both (max of left A <= min of right B) and (max of left B <= min of right A) will be false:
    1) A1 <= A2, B1 <= B2
    2) if A1 > B2
    3) then B1 <= B2 < A1 <= A2
    4) so there is no way B1 > A2 is true
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)

        # first make sure nums1 is shorter
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # then pick range
        low = 0 # left side is empty (everything including the first element belongs to right side)
        high = x # right side is empty (everything including the last element belongs to left side)
        while low <= high:
            partitionX = (low + high) // 2 # we turn nums1 into nums1[:partitionX] and nums1[partitionX:]
            partitionY = (x + y + 1) // 2 - partitionX 

            # next get the four numbers needed
            if partitionX == 0: # nothing for left side of x
                maxLeftX = -float("inf")
            else:
                maxLeftX = nums1[partitionX - 1]

            if partitionX == x: # nothing for right side of x
                minRightX = float("inf")
            else:
                minRightX = nums1[partitionX]

            if partitionY == 0: # nothing for left side of y
                maxLeftY = -float("inf")
            else:
                maxLeftY = nums2[partitionY - 1]

            if partitionY == y: # nothing for right side of x
                minRightY = float("inf")
            else:
                minRightY = nums2[partitionY]

            # last check two requirements and go into next loop
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0: 
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1


# TODO: this answer is not understood yet
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