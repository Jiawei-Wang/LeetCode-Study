class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            cur = 0
            for i in str(n):
                cur += int(i) * int(i)
            if cur in visited:
                return False
            n = cur
            visited.add(cur)
        
        return True


# 同样逻辑但是运行速度更快
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1


# 龟兔赛跑
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)
        
        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False
            
    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output