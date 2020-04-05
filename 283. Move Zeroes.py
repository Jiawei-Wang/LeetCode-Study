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
