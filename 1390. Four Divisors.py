# for a number > 1
# 1 and itself are 2 divisors
# so in order for it to have exactly 4 divisors
# it must have 2 other divisors, which are both prime numbers
# (prime numbers only have 2 divisors, noo prime number have more than 2)
# for example 
# 9 is not ok: 1, 9 and (3 * 3), only 3
# 10 is ok: 1, 10 and (2 * 5)
# 11 is not ok: 1, 11 and None, only 2
# 20 is not ok: 1, 20, and (2 * 10) and (4 * 5), more than 4
# so for each number, we need to see if there is 1 valid divisor between [1, Math.Sqrt(num)]
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            last_found = 0 
            divisor = 2 # start from 2 as smallest possible divisor
            while divisor * divisor <= num:
                if num % divisor == 0:
                    if last_found == 0:
                        last_found = divisor
                    else:
                        last_found = 0
                        break
                divisor += 1
            # above while loop marks the 2nd smallest divisor in a number that has either 3 or 4 divisors
            if last_found and last_found * last_found != num: # if a number has 3 divisors, the second one is Math.Sqrt(num)
                count += (1 + last_found + num // last_found + num)
        return count