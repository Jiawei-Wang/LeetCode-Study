# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo)//2 
            api = guess(mid)
            if api == 0:
                return mid
            elif api == -1:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        
        """
        there must a valid return value so:
        1. if we have 3 elements left: lo + 1 = mid = hi - 1: we can get a valid one using lo
        2. if we have 2 elements left: lo = mid = hi - 1: then api will never be -1
        """