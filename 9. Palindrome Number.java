// 将 x 转换为string
class Solution {
    public boolean isPalindrome(int x) {
        // integer to string: https://stackoverflow.com/questions/5071040/java-convert-integer-to-string
        String y = String.valueOf(x);

        // reverse string: https://www.geeksforgeeks.org/reverse-a-string-in-java/
        StringBuilder input1 = new StringBuilder();
        input1.append(y);
        String input2 = input1.reverse().toString();

        return input2.equals(y);
    }
}


// 解法2：不将 x 转换为string
class Solution {
    public boolean isPalindrome(int x) {
        // 如果数字为负数或者以0结尾，则直接返回false
        if ((x < 0) || (x != 0 && x % 10 == 0)) {
            return false;
        }

        int y = x;
        int z = 0;
        while (y != 0) {
            z = z * 10 + y % 10;
            y = y / 10;
        }

        return z == x;

    }
}
