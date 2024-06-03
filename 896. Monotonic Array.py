# 这个解法的巧妙之处在于不需要再额外判断是递增还是递减
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n <= 2: return True
				
        # 递增和递减默认都是False, 只要有一个元素符合要求, 就会被设置为永远为True
        isGreat = False
        isLess = False
        for i in range(1, n):
            if A[i - 1] > A[i]:
                isGreat = True
            if A[i - 1] < A[i]:
                isLess = True
            
            # 在任何一个位置上, 如果此时已经同时出现两个True, 则list不符合要求
            if isGreat and isLess:
                return False

        return True


# 2024
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = False
        is_decreasing = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                is_increasing = True
            elif nums[i] < nums[i-1]:
                is_decreasing = True
        
        return not (is_increasing and is_decreasing)
