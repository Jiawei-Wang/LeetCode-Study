# DP解题思路：1.找到转换公式，2.选择top-town/bottom-up，3.选择memo形式

# pure recursion：使用helper进行recursion
class Solution:
    # 主函数调用helper，然后传递必要的参数
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(n-1,m-1)

    # helper进行recursion
    def dp(self, n, m):
        # base case
        if n == 0 or m == 0:
            return 1

        if n > 0 and m > 0:
            return self.dp(n-1,m)+self.dp(n,m-1)

        # 别忘了把所有情况都囊括
        return 0
