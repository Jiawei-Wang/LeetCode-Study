# time nlogn space 1
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        return sorted(nums)


# time n space n
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = deque([])
        i = 0
        j = len(nums)-1
        while i <= j:
            left = nums[i] * nums[i]
            right = nums[j] * nums[j]
            # 不用考虑正负问题，因为一个数字的平方肯定不为负
            if left > right:
                ans.appendleft(left)
                i += 1
            else:
                ans.appendleft(right)
                j -= 1
        return ans


# 不用deque的方法：初始化一个list，所有元素均为0，然后同样用two pointer，每次找到位置然后更新


# 2024
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []

        l = 0
        r = len(nums)-1

        while l <= r:
            lo = nums[l]
            hi = nums[r]
            if abs(lo) < abs(hi):
                answer.append(hi * hi)
                r -= 1
            else:
                answer.append(lo * lo)
                l += 1
        
        return answer[::-1]