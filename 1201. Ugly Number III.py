# brute force
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        numbers = sorted([a,b,c])
        a = numbers[0]
        b = numbers[1]
        c = numbers[2]

        count = 0
        a_count = 1
        b_count = 1
        c_count = 1

        while count != n:
            count += 1
            nxt = min(a*a_count, b*b_count, c*c_count)
            if nxt == a*a_count:
                a_count += 1
            if nxt == b*b_count:
                b_count += 1
            if nxt == c*c_count:
                c_count += 1
        return nxt

        
"""
binary search:
basic idea: for any given integer N, it is easy to find total number of 
integers <= N that are divisible by a or b or c by doing some calculation
venn diagram: number = a + b + c - ac - ab - bc + abc
F(N) = N/a + N/b + N/c - N/lcm(a, c) - N/lcm(a, b) - N/lcm(b, c) + N/lcm(a, b, c)

least common multiple: smallest number that two or more numbers can divide into evenly
greatest common divisor: largest positive integer that divides each of the integers
lcm(a, b) = abs(a*b)//gcd(a,b)
"""
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # first find lcm
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, bc)
        
        # then binary search with the formula 
        lo, hi = 1, 2 * int(1e9) # from question constraints
        while lo < hi:
            mid = lo + (hi - lo) // 2
            count = (
                mid // a + mid // b + mid // c
                - mid // ab - mid // bc - mid // ac
                + mid // abc
            )
            if count < n:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
        