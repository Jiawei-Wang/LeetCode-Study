# built in
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# bitwise
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count
    
"""
理解：
bitwise AND：0 & 0 = 0, 0 & 1 = 0, 1 & 1 = 1
所以任何数字，比如：
00110101
和1：
00000001
做AND操作，得到的结果即为：如果最后一位为1则1，为0则0
所以while循环的意思是：
1. 如果n的最后一位为1，则count += 1
2. 将最后一位去掉（这里用的是 /2 的操作）
"""