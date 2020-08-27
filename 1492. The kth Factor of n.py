# brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        curr = 0
        for i in range(1, n+1):
            if n % i == 0:
                curr += 1
                if curr == k:
                    return i
        return -1


# improved brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # 直接使用 k 就可以少用一个变量
        # 只需要步进到 n/2，如果此时 k == 1，则下一个 factor 一定是 n 自身
        for i in range(1, n//2+1):
            if n % i == 0: k -= 1
            if k == 0: return i
        if k == 1:
            return n
        else:
            return -1
