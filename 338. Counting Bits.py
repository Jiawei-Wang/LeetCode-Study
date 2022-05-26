# brute force
# n^2
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(str(bin(i)).count('1'))
        return ans


# time nlogn
# 一个十进制数字中二进制'1'的数量可以这样计算：
# 例：7 -> 7%2=1, 3%2=1, 1%2=1, 0 stop, so in total three '1's in 7. time logn
class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(i):
            cnt = 0
            while i:
                cnt += i%2
                i //= 2
            return cnt
        ans = []
        for i in range(n+1):
            ans.append(helper(i))
        return ans


# dp: time n
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp