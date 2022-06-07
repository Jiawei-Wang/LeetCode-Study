# space n 解法：hashmap/dict，或者hashset
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)


# XOR: 0^0 = 0, 0^1 = 1, 1^1 = 0
# 逻辑：偶数个数的数字会互相cancel，最后每位都是0，与single one做XOR操作，返回值为single one
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


# XOR语法的其他写法：

# functools.reduce(fun,seq) applies a particular function passed in its argument to all of the list elements mentioned in the sequence passed along
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
        
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)

