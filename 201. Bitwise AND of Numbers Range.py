class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 给定一个范围，将范围内所有数字转化为二进制并进行and运算，得到的值返回其十进制值
        # Bitwise AND operator: Returns 1 if both bits are 1 else 0.
        # 所以对于一组binary，意味着如果在这一位上它们全都是1,才能返回1,否则0

        # 解法1：从m开始，每次挪一位（二进制中位数提高一位，值变成两倍）
        res, move = m, 1
        while res + move <= n:
            res &= res + move
            move *= 2
        return res & n

        # 解法2：对于每一位而言，其改变一次，后面一位需要改变2次，再后一位需要4次，等等
        # the bitwise and of the range is keeping the common bits of m and n from left to right until the first bit that they are different
        # padding zeros for the rest.
        i = 0
        while m != n:
            # right shift：最右边n位的数字丢弃，从左边插入n个0,这里n=1
            # 如果两个数在末位不同，则末位为0，然后向左移一位
            m >>= 1
            n >>= 1
            i += 1
        # 找到相同的部分，返回这部分加上右边所有的0
        return n << i
