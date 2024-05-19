"""
下面这个解法是正确的，它适用的是每个值均出现一次，另有一个值出现2次的情况，比如：[1,2,3,4,5,6,3]
但是针对本题是错误的，因为本题的条件为：每个元素都在范围内，但并不代表每个值都会出现，且重复的那个值，可能会出现多于2次的情况，比如：[2,2,2,2,2,2]
"""
# xor
# 因为我们有 n+1 个元素，每个的值在[1,n]之间，所以xor最后可以得到: xor = (last index + 1) ^ 多余的那个元素
# 因为xor的反向式依旧为xor (a^b=c, 则c^b=a)，所以可以得到重复的元素
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        for i in range(n):
            xor = xor ^ (i+1) ^ nums[i]
        
        return xor ^ n


# 暴力解：sort，然后找重复
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]
        return -1


# 暴力解：用set，遍历找重复
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Map = {}
        for i in nums:
            if i in Map:
                return i
            Map[i] = 1
        return -1


# 暴力解：对所有两两组合进行对比
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1


# 转换思路：我们要找到一个值，验证它在list中是否有重复，而不是在list中找到两个元素，它们的值相同
# binary search，但是是针对value，而不是index
# 假设value的范围是[1,9]，那么猜5，查看list中小于5，大于5的元素分别有多少个，哪边数量多于一半，则重复的元素一定是在这个取值范围内
# time nlogn
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n-1

        while left <right:
            mid = left + (right -left) //2 
            counter = 0
            for i in range(n):
                if nums[i] <= mid:
                    counter +=1
            if counter > mid:
                right = mid
            else:
                left = mid + 1
        return left


# 将index和value都视为一个linked list node，比如nums=[1,2]，可以视为 0 -> 1, 1 -> 2
# 如果有重复元素，则linked list肯定有环
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
    
"""
对于两个while循环的解释：
To understand this solution, you just need to ask yourself these question.
Assume the distance from head to the start of the loop is x1
the distance from the start of the loop to the point fast and slow meet is x2
the distance from the point fast and slow meet to the start of the loop is x3

What is the distance fast moved?
x1 + x2 + x3 + x2
What is the distance slow moved? 
x1 + x2
And their relationship?
x1 + x2 + x3 + x2 = 2 (x1 + x2)

Thus x1 = x3, that's the reason we reset slow to be 0.
"""