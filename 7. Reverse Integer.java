// 解法：逐位剥离
// Time：数字 X 大约有 log10（X）位，所以时间复杂度为：logX
class Solution {
    public int reverse(int x) {
        // rev存储的是逐位反转后的数字
        int rev = 0;
        while (x != 0) {
            // pop存储的是当前X的最后一位
            int pop = x % 10;
            x /= 10;
            // 特别注意点：overflow的检查
            // Integer.MAX_VALUE: 2^31-1 = 2147483647
            // Integer.MIN_VALUE: -2^31 = -2147483648
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
