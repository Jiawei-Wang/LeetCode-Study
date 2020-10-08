# 解法1：使用新的array
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 创建一个新array
        newArray = [-1] * len(nums)
        # 遍历nums，如果元素非0，放进新array，同时统计0的总数
        totalZero = 0;
        for i in range(len(nums)):
            if nums[i] == 0:
                totalZero += 1
            else:
                newArray[i-totalZero] = nums[i]
        # 把新array的尾部填充满0
        for j in range(len(nums)-totalZero, len(nums)):
            newArray[j] = 0
        # 把新array的值给nums
        for i in range(len(nums)):
            nums[i] = newArray[i]


# 解法2：非0元素往前放，尾部用0填充
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_zero] = nums[i]
                last_zero += 1
        for i in range(last_zero, len(nums)):
            nums[i] = 0


# 解法3：
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

"""
分析：
两个指针，一个遍历元素，另一个先按顺序遍历直到找到第一个0
在这个0后面的元素会出现两种情况：不为0和为0
如果后面的元素不为0，则将二者的值交换，并把指针加1 （实现的是把后面第一个不为0的元素放在第一个0前面）
如果后面的元素为0，则什么都不做（即两个0并排放在一起），继续寻找下一个元素
用一个具体例子来形容：在找到第一个0之前所有元素不动，在找到0之后，遇到非0元素就抽出来放在0前面，遇到0就叠加在一起继续往后推
"""
