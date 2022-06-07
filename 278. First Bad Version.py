# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 我们想在一个list中找到第一个T：[F,F,T,T,T,T]
        left, right = 1, n # 下标是1到n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid): 
                right = mid # 我们不知道mid-1是否为T
            else:
                left = mid + 1 # 我们知道T至少是从mid+1开始
        return left
