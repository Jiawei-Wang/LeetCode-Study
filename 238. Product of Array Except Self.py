class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 限制条件： 1.不使用除法  2.O(n)  3.O(1)space

        # 算法1：使用两个list记录每个元素左边和右边的乘积，相乘得到该元素的值
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        # 第一个元素左边没有乘积，默认为1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer

# O(1) space approach
# 算法如下：用list从左到右记录每个数字左边的乘积，然后再用一个从右到左的pointer记录每个数字右边的乘积并和list相乘
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0]*length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
