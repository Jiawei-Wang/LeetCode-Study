// 这道题考察的是进制转换，所以 ZY = 26 * 26 + 25 = 701
class Solution {
    public int titleToNumber(String s) {
        int result = 0;
        // 学习新的for循环写法
        for (int i = 0; i < s.length(); result = result * 26 + (s.charAt(i) - 'A' + 1), i++);
        return result;
    }
}
