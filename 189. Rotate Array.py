"""
python中对于list的操作：
a = [1,2,3,4]           地址1
a = a[:2]+a[2:]         地址2
a[:] = a[:2]+a[2:]      地址1
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]


# 上面这个答案需要O(n) space：用于保存两个片段

# 将每个片段单独翻转
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)