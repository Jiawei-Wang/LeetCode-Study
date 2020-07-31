# 解法1：使用string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # int to string
        y = str(x)

        # reverse string: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
        z = y[::-1]

        return y == z


# 解法2：不用string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return rev == x or x == rev//10
        
