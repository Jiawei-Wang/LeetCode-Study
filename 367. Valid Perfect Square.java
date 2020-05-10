class Solution {
    public boolean isPerfectSquare(int num) {
        // 1 + 3 + 5 + 7 + 9 + ...
         int i = 1;
         while (num > 0) {
             num -= i;
             i += 2;
         }
         return num == 0;
    }
}
