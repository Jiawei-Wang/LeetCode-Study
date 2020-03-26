class Solution {
    public int findComplement(int num) {

        // total是大于等于十进制的num的多个1组成的数字的对应二进制数
        // 例：num = 27 (11011)，那么total = 31 （11111）
        int total = 0;

        int digit = 0;

        // 二进制的 11111 代表十进制的 2^4 + 2^3 + 2^2 + 2^1 + 2^0
        while (total < num) {
            total += Math.pow(2, digit);
            digit += 1;
        }
        return total-num;
    }
}

// 本题的核心是二进制转换成十进制后，加减法结果相同
// 例：11111 - 11011 = 100 （31 - 27 = 4）
