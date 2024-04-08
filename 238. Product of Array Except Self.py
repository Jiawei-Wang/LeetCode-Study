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


# 04/26/2022 重新回顾此题
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        限制：不可以用除法，复杂度限制为n
        一些想法：
        最开始想到的是使用类似滑动窗口的方式，每次乘一个新的元素，并除去一个旧的元素，但发现这依旧使用了除法，其次是元素可能为0，除法会报错
        暴力解不用除法，但复杂度为n^2
        '''
        
        # 解法1：使用除法，time n, space n
        # 三个case：
        # list中没有0：total//元素
        # list中一个0：除了0对应位置为total，其他均为0
        # list中超过一个0：所有元素均为0
#         zero_count = 0
#         zero_index = -1
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 zero_count += 1
#                 zero_index = i
                
#         if zero_count > 1:
#             return [0 for _ in range(len(nums))]
#         elif zero_count == 1:
#             total = 1
#             for i in range(len(nums)):
#                 if i != zero_index:
#                     total *= nums[i]
#             return [0 for _ in range(zero_index)] + [total] + [0 for _ in range(zero_index+1, len(nums))]
        
#         total = 1
#         for i in nums:
#             total *= i
#         return [total//x for x in nums]
    
        # 对解法1的代码优化：time n space 1
        # total = functools.reduce(lambda a, b: a*(b if b else 1), nums, 1) # 获得total
        # '''
        # 对于functools.reduce()的解释：https://www.geeksforgeeks.org/reduce-in-python/
        # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
        # 对于reduce()中第三个参数‘1’的解释：
        # If the optional initializer is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty. 
        # If initializer is not given and sequence contains only one item, the first item is returned.
        # '''
        # zero_count = nums.count(0) # 获得zero_count
        # if zero_count > 1: 
        #     return [0]*len(nums)
        # for i, c in enumerate(nums): # about enumerate(): https://www.geeksforgeeks.org/enumerate-in-python/
        #     if zero_count: 
        #         nums[i] = 0 if c else total # rewrite on original list, save space
        #     else: nums[i] = total // c
        # return nums

        # solution 2: prefix * suffix
        # time n, space n
        pre = list(itertools.accumulate(nums, operator.mul))
        suf = list(itertools.accumulate(nums[::-1], operator.mul))[::-1]
        # itertools.accumulate(): makes an iterator that returns the results of a function.
        # accumulate() vs reduce(): https://stackoverflow.com/questions/14132545/itertools-accumulate-versus-functools-reduce
        length = len(nums)
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < length else 1) for i in range(length)] # 首尾两个元素的各自prefix和suffix要单独对待
        
        '''
        对解法2仍有两种进一步优化的方式，下次再学习
        https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach
        '''


"""
2024
"""
# prefix and postfix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) # length >= 2 given by question

        left = []
        l = 1
        for num in nums:
            l *= num
            left.append(l)

        right = []
        r = 1
        for num in nums[::-1]:
            r *= num
            right.append(r)
        right.reverse()

        answer = []
        answer.append(right[1])
        for i in range(1, length-1):
            answer.append(left[i-1]*right[i+1])
        answer.append(left[-2])
        return answer


# O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        # store prefix directly in the answer 
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # then multiply by postfix and get the answer
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        