# 解法1：brute force，挨个修改array A中的元素，查看array是否符合要求
# Time: n^2
# Space: n
class Solution:
    def checkPossibility(self, A):

        # helper：检查输入array是否是non decreasing，如果不是，返回False
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        new = A[:]
        for i in range(len(A)):
            # 使用变量暂存原始数据
            old_ai = A[i]
            # 如果是0号元素，则设为无穷小
            new[i] = new[i-1] if i > 0 else float('-inf')
            # 如果通过修改一个元素，使得array符合要求，则返回True
            if monotone_increasing(new):
                return True
            # 把被修改的元素还原
            new[i] = old_ai

        return False


# O(n)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        
        # 检查每一对元素
        for i in range(len(nums)-1):
            # 如果是非递减则符合条件，直接跳过
            if nums[i] <= nums[i+1]:
                continue
            # 如果是递减且此时仅有一次的修改机会已被使用，则返回False
            if changed:
                return False
            # 如果是递减且此时修改机会还未被使用，则修改元素
            # 修改的原则为：
            # 1. 尽可能修改前者，让前者的值和后者保持一致
            # 2. corner case：[3, 4, 2]，那么就不能让4变为2，而是要让2变为4（即修改后者）
            if i == 0 or nums[i+1] >= nums[i-1]: # 如果前者前面没其他元素，或者有允许前者修改的空间，则修改前者
                nums[i] = nums[i+1]
            else: # 如果无法修改前者，则修改后者
                nums[i+1] = nums[i]
            
            changed = True
            
        return True