# math: a square number is 1 + 3 + 5 + 7 + ...
# time: O(sqrt(n))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0 


# binary search
# time O(logn)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False