# bin(i): 将i（必须是integer）转换为二进制，例：bin(5) = 0b101
# int(i, 2)：将i（必须是string）转换为十进制，例：int('101', 2) = 5, int('0b101', 2) = 5

# remove digit from n's end, append it to result's end
class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        result = 0 # 0000_0000_0000_0000_0000_0000_0000_0000
        for i in range(32): 
            result <<= 1 # 在最末尾插入一个0
            # in first loop: 0 <<= 1 is still 32 digits of 0s
            
            if (n & 1) == 1: # 如果n的最末尾为1
            # 0101 (first 3 digis don't matter) & 0001 = 1 
            # 0100 & 0001 = 0
                result += 1 # 将最末尾更新为1

            n >>= 1 # 删去最末尾的数字
        return result