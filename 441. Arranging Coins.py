class Solution:
    def arrangeCoins(self, n: int) -> int:
        def is_valid(k):
            total = (1+k)/2*k
            if total <= n:
                return True
            else:
                return False
        
        lo = 1
        hi = n
        while lo < hi:
            if lo == hi - 1:
                return hi if is_valid(hi) else lo

            mid = lo + (hi-lo)//2
            if is_valid(mid):
                lo = mid
            else:
                hi = mid - 1
        
        return lo


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l+r)//2
            coins = (mid+1)/2*mid
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res