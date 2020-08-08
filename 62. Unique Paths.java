// pure recursion
class Solution {
    public int uniquePaths(int m, int n) {
        return dp(m - 1, n - 1);
    }

    private int dp(int m, int n) {
        if (m == 0 || n == 0) {
            return 1;
        }
        if (m > 0 && n > 0) {
            return dp(m - 1, n) + dp(m, n - 1);
        }
        return 0;
    }
}
