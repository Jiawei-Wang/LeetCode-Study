# bin(i): 将i（必须是integer）转换为二进制，例：bin(5) = 0b101
# int(i, 2)：将i（必须是string）转换为十进制，例：int('101', 2) = 5, int('0b101', 2) = 5

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        result = 0
        for i in range(32):
            result <<= 1 # 在最末尾插入一个0
            if (n & 1) == 1: # 如果n的最末尾为1
                result += 1 # 将最末尾更新为1
            n >>= 1 # 删去最末尾的数字
        return result